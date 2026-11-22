import html
import json
import os
import re
import tempfile
import time
from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo, tooltip, askUser
from anki.hooks import addHook
#test
try:
    from aqt.theme import theme_manager
except Exception:  # very old Anki
    theme_manager = None


def _night_mode():
    return bool(getattr(theme_manager, "night_mode", False))

try:  # Anki 2.1.50+ (PyQt6)
    from PyQt6.QtWebEngineCore import QWebEnginePage
    from PyQt6.QtWebEngineWidgets import QWebEngineView
except ImportError:  # older Anki (PyQt5)
    from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

# ==========================================
# PART 1: CONSTANTS
# ==========================================

ADDON_NAME = "MedFlow"
MODEL_NAME = "MedFlow"
EDITOR_FILE = "medflow_editor.html"
BRIDGE_PREFIX = "__medflow__:"
SHARED_JS_TOKEN = "/*MF_SHARED*/"
# `user_files` is kept by Anki when the add-on is updated, so the user's templates survive updates.
USER_DIR = os.path.join(os.path.dirname(__file__), "user_files")
TEMPLATES_FILE = os.path.join(USER_DIR, "templates.json")

# ==========================================
# PART 2: NOTE TYPE INSTALLER
# ==========================================
def _read_addon_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _load_card_templates():
    """Returns (front, back). The shared rendering JS is injected into both templates."""
    source = _read_addon_file("card_templates.html")

    def extract(start_marker, end_marker):
        start = source.index(start_marker) + len(start_marker)
        end = source.index(end_marker, start)
        return source[start:end].strip()

    shared = extract("<!-- SHARED_JS_START -->", "<!-- SHARED_JS_END -->")
    front = extract("<!-- FRONT_TEMPLATE_START -->", "<!-- FRONT_TEMPLATE_END -->").replace(SHARED_JS_TOKEN, shared)
    back = extract("<!-- BACK_TEMPLATE_START -->", "<!-- BACK_TEMPLATE_END -->").replace(SHARED_JS_TOKEN, shared)
    return front, back


def install_model():
    css = _read_addon_file("style.css")
    front, back = _load_card_templates()
    m = mw.col.models.by_name(MODEL_NAME)

    if not m:
        mm = mw.col.models.new(MODEL_NAME)
        mm['type'] = 1  # cloze
        mw.col.models.add_field(mm, mw.col.models.new_field("Text"))
        mw.col.models.add_field(mm, mw.col.models.new_field("Algorithm_JSON"))
        mw.col.models.add_field(mm, mw.col.models.new_field("Extra"))
        mm['css'] = css
        t = mw.col.models.new_template("Card 1")
        t['qfmt'] = front
        t['afmt'] = back
        mw.col.models.add_template(mm, t)
        mw.col.models.add(mm)
        return

    # Existing note type: refresh it from the add-on files, but only save when something changed.
    changed = False
    if m.get('css') != css:
        m['css'] = css
        changed = True
    tmpls = m['tmpls']
    if tmpls and (tmpls[0]['qfmt'] != front or tmpls[0]['afmt'] != back):
        tmpls[0]['qfmt'] = front
        tmpls[0]['afmt'] = back
        changed = True
    if changed:
        mw.col.models.save(m)

addHook("profileLoaded", install_model)

# ==========================================
# PART 3: ADD-ON LOGIC
# ==========================================

# ---- Embedded editor window -------------------------------------------------

_open_windows = []  # keeps references so the windows are not garbage collected

# < > & are written as \\uXXXX escapes (still valid JSON): Anki's field editor treats the field as HTML and
# would otherwise mangle the formatting tags stored inside the JSON.
GET_DATA_JS = r"""(typeof syncHeights === 'function' && syncHeights(), JSON.stringify({nodes: ns, edges: es}).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026'))"""


def _encode_json(obj):
    """Same escaping as GET_DATA_JS, for JSON produced on the Python side."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def _field_name(note, name, index):
    """Field called `name`, or the field at `index` for notes using a different note type."""
    if name in note:
        return name
    keys = note.keys()
    return keys[index] if len(keys) > index else None


def _get_json_field(editor):
    """Returns the raw content of the Algorithm_JSON field (or the 2nd field)."""
    f = _field_name(editor.note, "Algorithm_JSON", 1)
    return (editor.note[f] or "{}") if f else "{}"


def _set_json_field(editor, value):
    f = _field_name(editor.note, "Algorithm_JSON", 1)
    if f:
        editor.note[f] = value
    editor.loadNote()


def _clean_json(raw):
    """The field may contain HTML (<br>, &nbsp;...) - strip it before parsing."""
    raw = re.sub(r"<br\s*/?>", "", raw or "", flags=re.I)
    raw = raw.replace("&nbsp;", " ")
    raw = re.sub(r"<[^>]*>", "", raw)
    raw = raw.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&")
    return raw.strip()


def _add_to_media(path):
    media = mw.col.media
    add = getattr(media, "add_file", None) or media.addFile
    return add(path)


IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp")


def _read_templates():
    """Raw JSON text of the saved templates ('' when nothing was saved yet)."""
    try:
        with open(TEMPLATES_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def _write_templates(text):
    try:
        json.loads(text)  # never store something that cannot be read back
        os.makedirs(USER_DIR, exist_ok=True)
        tmp = TEMPLATES_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, TEMPLATES_FILE)
        return True
    except Exception as e:
        showInfo(f"Could not save the templates: {e}")
        return False


def _images_from_clipboard():
    """Image data (screenshot / copied image) or copied image files -> Anki media names."""
    md = QApplication.clipboard().mimeData()
    if md is None:
        return []
    names = []
    if md.hasUrls():  # files copied in the file manager
        for url in md.urls():
            p = url.toLocalFile()
            if p and p.lower().endswith(IMAGE_EXTS) and os.path.isfile(p):
                names.append(_add_to_media(p))
        if names:
            return names
    if md.hasImage():
        img = QApplication.clipboard().image()
        if not img.isNull():
            tmp = os.path.join(tempfile.gettempdir(), "medflow_%d.png" % int(time.time() * 1000))
            if img.save(tmp, "PNG"):
                try:
                    names.append(_add_to_media(tmp))
                finally:
                    if os.path.exists(tmp):
                        os.remove(tmp)
    return names


class MedFlowPage(QWebEnginePage):
    """Lets the editor page talk to Python through prompt('__medflow__:<cmd>')."""

    def __init__(self, parent_widget, parent=None):
        super().__init__(parent)
        self.parent_widget = parent_widget

    def javaScriptPrompt(self, origin, msg, default):
        if not msg.startswith(BRIDGE_PREFIX):
            return super().javaScriptPrompt(origin, msg, default)
        cmd = msg[len(BRIDGE_PREFIX):]
        if cmd == "tpl_load":
            return True, _read_templates()
        if cmd == "tpl_save":  # the JSON travels in the prompt's default value
            return True, "ok" if _write_templates(default) else "error"
        names = []
        try:
            if cmd == "pick":
                files, _ = QFileDialog.getOpenFileNames(
                    self.parent_widget, "Choose image", "",
                    "Images (*.png *.jpg *.jpeg *.gif *.webp *.svg *.bmp)")
                names = [_add_to_media(f) for f in files]
            elif cmd == "pasteimg":
                names = _images_from_clipboard()
        except Exception as e:
            showInfo(f"Could not add the image: {e}")
        return True, json.dumps(names)


class FlowchartDialog(QDialog):
    def __init__(self, editor, initial_json):
        super().__init__(editor.widget)
        self.editor = editor
        self.initial_json = initial_json
        self._loaded_state = None
        self._force_close = False

        self.setWindowTitle(ADDON_NAME)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.resize(1280, 800)

        self.web = QWebEngineView(self)
        self.web.setPage(MedFlowPage(self, self.web))
        self._dark = _night_mode()
        if self._dark:
            self.web.page().setBackgroundColor(QColor("#161a24"))

        self.btn_save = QPushButton("Save to note")
        self.btn_sync = QPushButton("Save and generate cards")
        self.btn_cancel = QPushButton("Close")
        self.btn_save.setShortcut(QKeySequence("Ctrl+S"))
        self.btn_save.clicked.connect(lambda: self._save(sync=False))
        self.btn_sync.clicked.connect(lambda: self._save(sync=True))
        self.btn_cancel.clicked.connect(self.close)

        bar = QHBoxLayout()
        bar.setContentsMargins(8, 6, 8, 6)
        bar.addStretch(1)
        bar.addWidget(self.btn_cancel)
        bar.addWidget(self.btn_save)
        bar.addWidget(self.btn_sync)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.web, 1)
        layout.addLayout(bar)

        self.web.loadFinished.connect(self._on_loaded)
        path = os.path.join(os.path.dirname(__file__), EDITOR_FILE)
        self.web.load(QUrl.fromLocalFile(path))

    # -- loading -------------------------------------------------------------
    def _on_loaded(self, ok):
        if not ok:
            showInfo("Could not load the editor.")
            return
        media_url = QUrl.fromLocalFile(mw.col.media.dir()).toString().rstrip("/") + "/"
        js = (
            "(function(){"
            "var d = JSON.parse(%s);"
            "ns = Array.isArray(d.nodes) ? d.nodes : [];"
            "es = Array.isArray(d.edges) ? d.edges : [];"
            "window.MEDFLOW_MEDIA_URL = %s;"
            "document.documentElement.setAttribute('data-theme', %s);"
            "clearSel(); resetHistory(); render();"
            # the native buttons below replace the clipboard-based Save/Copy
            "var b = document.querySelector('#toolbar .save'); if (b) b.style.display = 'none';"
            "})();"
        ) % (json.dumps(self.initial_json), json.dumps(media_url), json.dumps("dark" if self._dark else "light"))
        self.web.page().runJavaScript(js)
        self.web.page().runJavaScript(GET_DATA_JS, self._remember_state)

    def _remember_state(self, state):
        self._loaded_state = state

    # -- saving --------------------------------------------------------------
    def _save(self, sync):
        def done(state):
            if not state:
                showInfo("Could not read the data from the editor.")
                return
            _set_json_field(self.editor, state)
            self._loaded_state = state
            self._force_close = True
            self.close()
            if sync:
                sync_cards(self.editor)
            else:
                tooltip("Flowchart saved to the Algorithm_JSON field.")

        self.web.page().runJavaScript(GET_DATA_JS, done)

    # -- closing (warn about unsaved changes) --------------------------------
    def closeEvent(self, event):
        if self._force_close:
            if self in _open_windows:
                _open_windows.remove(self)
            event.accept()
            return
        event.ignore()

        def check(state):
            if state is None or state == self._loaded_state:
                self._force_close = True
                self.close()
            elif askUser("You have unsaved changes. Close anyway?", parent=self):
                self._force_close = True
                self.close()

        self.web.page().runJavaScript(GET_DATA_JS, check)


def open_ext(editor):
    path = os.path.join(os.path.dirname(__file__), EDITOR_FILE)
    if not os.path.isfile(path):
        showInfo(EDITOR_FILE + " was not found in the add-on folder.")
        return

    raw = _clean_json(_get_json_field(editor))
    try:
        parsed = json.loads(raw) if raw and raw != "null" else {}
        if not isinstance(parsed, dict):
            parsed = {}
    except Exception:
        if not askUser("The Algorithm_JSON field does not contain valid JSON. Open an empty editor?"):
            return
        parsed = {}

    dlg = FlowchartDialog(editor, json.dumps(parsed))
    _open_windows.append(dlg)
    dlg.showMaximized()


# ---- Card generation ----------------------------------------------------------

def _cloze_of(node):
    try:
        return int(node.get("cloze", 0) or 0)
    except (TypeError, ValueError):
        return 0


def sync_cards(editor):
    editor.saveNow(lambda: _sync_logic(editor))


def _sync_logic(editor):
    note = editor.note
    json_field = _field_name(note, "Algorithm_JSON", 1)
    text_field = _field_name(note, "Text", 0)
    data_str = _clean_json(note[json_field]) if json_field else ""
    if not data_str or data_str == "null":
        tooltip("The Algorithm_JSON field is empty.")
        return

    try:
        data_obj = json.loads(data_str)
    except Exception as e:
        showInfo(f"Invalid JSON in the Algorithm_JSON field: {e}")
        return

    nodes = data_obj.get("nodes", []) if isinstance(data_obj, dict) else []
    used = sorted({_cloze_of(n) for n in nodes if _cloze_of(n) > 0})
    if not used:
        showInfo("No clozes found. Give at least one box a cloze number in the editor.")
        return

    notes_to_user = []

    # Gaps in the numbering (c1, c3, c7...) are harmless for existing notes, because the review
    # history of each card is tied to its number. For a brand new note nothing is tied yet,
    # so the numbers are compacted to 1..N.
    gaps = used != list(range(1, len(used) + 1))
    is_new_note = not getattr(note, "id", 0)
    if gaps and is_new_note:
        mapping = {old: new for new, old in enumerate(used, start=1)}
        for n in nodes:
            if _cloze_of(n) > 0:
                n["cloze"] = mapping[_cloze_of(n)]
        note[json_field] = _encode_json(data_obj)
        notes_to_user.append("cloze numbers were renumbered to 1-%d" % len(used))
        used = sorted(mapping.values())
    elif gaps:
        notes_to_user.append("cloze numbers have gaps (%s); cards are only created for used numbers"
                             % ", ".join("c%d" % c for c in used))

    # Cloze numbers that existed before but are no longer used leave empty cards behind.
    removed = set()
    if not is_new_note and text_field:
        previous = {int(c) for c in re.findall(r"\{\{c(\d+)::", note[text_field] or "")}
        removed = previous - set(used)

    trigger_str = "".join(f"{{{{c{c}::CLOZEID_{c}}}}} " for c in used)

    # Reference the extra images in a field so Anki's media check, exports and
    # shared decks keep them (hidden: they are only used by the back of the card).
    images = []
    for n in nodes:
        for f in n.get("images", []) or []:
            if f not in images:
                images.append(f)
        src = n.get("src")
        if src and src not in images:
            images.append(src)
    for f in images:
        trigger_str += f'<img src="{html.escape(f, quote=True)}" style="display:none"> '

    if text_field:
        note[text_field] = trigger_str
    editor.loadNote()

    msg = f"Success! {len(used)} card(s) generated"
    if notes_to_user:
        msg += " (" + "; ".join(notes_to_user) + ")"
    tooltip(msg + ".")

    if removed:
        showInfo("These cloze numbers are no longer used: %s.\n"
                 "Their cards will now be empty. Remove them with Tools > Empty Cards."
                 % ", ".join("c%d" % c for c in sorted(removed)))


def add_btns(buttons, editor):
    b1 = editor.addButton(icon=None, cmd="alg_open", func=lambda e=editor: open_ext(e), tip="Open Flowchart Editor", label="Alg")
    buttons.append(b1)
    return buttons

addHook("setupEditorButtons", add_btns)
