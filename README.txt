# MEDFlow – Interactive Medical Flowcharts & Cloze Flashcards

> **Think Visually. Learn Actively. Remember More.**

MEDFlow is an Anki add-on that transforms complex medical concepts into interactive flowcharts and Cloze flashcards.

Build diagnostic algorithms, organize clinical reasoning, connect visual elements, and turn your diagrams into active-recall cards — all directly inside Anki.

Inspired by **ZeestMedical**, MEDFlow was independently developed to provide an integrated and enhanced flowchart creation and review experience.

---

## ✨ Features at a Glance

- 🎨 **Interactive Flowchart Editor** – Build diagrams using Steps, Decisions, and Information boxes.
- 🔗 **Clinical Connections** – Create and customize arrows, labels, and decision pathways.
- 🖼️ **Image Nodes** – Insert, resize, connect, and display images directly inside flowcharts.
- 🃏 **Cloze Generation** – Transform flowchart elements into individual Anki Cloze cards.
- 🎯 **Focus Flow** – Review selected branches progressively, one Cloze at a time.
- 📱 **Mobile Optimization** – Improved visualization and interaction on smaller screens.
- 💡 **Box Hints** – Reveal contextual hints without immediately exposing answers.
- 📝 **Extra Content** – Attach explanations, notes, and complementary images.
- 📚 **Templates** – Save, reuse, and organize flowchart models.
- ↩️ **Undo / Redo** – Maintain up to 200 editing states.
- 📤 **Import / Export** – Save and share diagrams using JSON files.
- 🌙 **Dark Mode** – Compatible with Anki's dark theme.

---

## 📸 Screenshots & Demonstrations

<!-- Add your screenshots and GIFs below -->

### Flowchart Editor

<!-- 📷 INSERT EDITOR SCREENSHOT OR GIF -->

### Cloze Flashcard Review

<!-- 📷 INSERT FRONT/BACK REVIEW GIF -->

### Image Nodes

<!-- 📷 INSERT IMAGE NODES DEMONSTRATION -->

### Focus Flow

<!-- 📷 INSERT FOCUS FLOW DEMONSTRATION -->

### Mobile Review

<!-- 📷 INSERT MOBILE REVIEW SCREENSHOT -->

---

## 🧠 How MEDFlow Works

MEDFlow combines visual diagram creation with Anki's spaced repetition system.

1. Create a flowchart using the integrated editor.
2. Add clinical steps, decisions, and information.
3. Connect elements to build diagnostic or therapeutic pathways.
4. Assign Cloze numbers to the elements you want to memorize.
5. Save the diagram and generate your Anki cards.
6. Review your cards using the complete flowchart or Focus Flow.

Each Cloze number generates a corresponding card. Elements sharing the same number are tested together.

---

## 🎨 Interactive Flowchart Editor

Create and organize medical algorithms using three element types:

| Element | Purpose |
|---|---|
| Step / Box | Clinical stages, procedures, findings, and actions |
| Decision | Clinical decisions and branching points |
| Information | Additional explanations and important details |

The editor includes:

- Free positioning and resizing.
- Automatic alignment guides.
- Multiple selection and simultaneous editing.
- Customizable colors, borders, and typography.
- Individual formatting for boxes and connections.
- XMind-inspired keyboard shortcuts.
- Undo and redo history.

### Connections

- Draggable blue connection points.
- Parent-child relationships.
- Reconnectable arrows.
- Customizable arrow styles.
- Editable labels such as Yes, No, Positive, and Negative.
- Link Mode for creating connections.

---

## 🖼️ Image Nodes

Image Nodes allow you to insert images directly into the flowchart as independent visual elements.

Unlike images attached through Extra, these images become part of the diagram itself.

Features:

- Paste images directly into the editor.
- Resize and reposition images freely.
- Connect images to other elements.
- Add image captions.
- Display images in generated Anki cards.
- Automatically hide captions when their corresponding images are hidden by Cloze.

Useful for anatomy, histology, radiology, pathology, dermatology, and other visually oriented subjects.

---

## 🃏 Cloze Flashcards

Assign Cloze numbers to individual flowchart elements.

For example:

- Element 1 → c1
- Element 2 → c2
- Element 3 → c3

Elements with the same Cloze number are tested together.

During review:

- The complete flowchart remains available.
- The active Cloze element receives visual emphasis.
- Hidden elements can be revealed by clicking.
- The diagram can be reviewed in its entirety or through Focus Flow.

Use **Save and Generate Cards** to save your diagram and generate the corresponding cards.

---

## 🎯 Focus Flow

Focus Flow allows you to isolate and progressively review specific branches of a flowchart.

Instead of reviewing the entire algorithm at once, you can select a pathway and follow its elements step by step.

### Setup

1. Select the boxes belonging to a branch using Shift + Click or Shift + Drag.
2. Alternatively, select only the starting box to include its connected downstream elements automatically.
3. Activate Focus using the target button or `Ctrl + Shift + F`.
4. Selected elements receive a visual Focus indicator.

### During Review

- The selected branch starts from its initial element.
- Relevant elements are presented progressively.
- Arrows guide the pathway.
- Unrelated branches remain hidden.
- Elements without Cloze remain visible alongside related elements.
- Cards without Focus settings continue displaying the complete diagram.

You can switch between the focused branch and the complete flowchart using the eye and target controls.

---

## 📱 Mobile Review

MEDFlow includes improvements for reviewing complex flowcharts on smaller screens.

- Automatic screen adaptation.
- Prioritization of the active Cloze element.
- Improved zoom and centering.
- Full-flowchart viewing when needed.
- Adaptation to screen resizing and orientation changes.
- Touch-friendly controls.

Designed to improve readability on mobile Anki clients, including AnkiMobile.

---

## 💡 Box Hints & 📝 Extra Content

### Box Hints

Add contextual hints to individual boxes.

- Hints appear in green above elements in the editor.
- A **+** button appears during review when the corresponding element is hidden.
- Click to reveal the hint in place of the hidden content.
- Click again to hide it.

### Extra

Attach complementary content to individual elements.

- Clinical explanations.
- Detailed notes and observations.
- Additional images.
- Supporting information displayed on the back of the corresponding Cloze card.

---

## 📚 Templates

Templates allow you to reuse frequently needed flowchart structures.

- Use predefined templates.
- Save custom templates.
- Save selected boxes or entire diagrams.
- Reuse templates in other notes.
- Restore original templates.
- Keep custom templates stored separately from editor files to help preserve them during updates.

---

## 🧭 Navigation & Customization

- Zoom in and out.
- Fit the complete flowchart to the workspace.
- Pan by dragging the background.
- Zoom around the cursor using Ctrl + Mouse Wheel.
- Multiple selection.
- Automatic alignment guides.
- Collapsible sidebar.
- Customizable box and arrow appearance.
- Rich-text formatting.
- Dark mode compatibility.
- Preserve zoom and canvas position between card sides and cards during the same review session.

---

## 📤 Import, Export & Storage

MEDFlow supports JSON import and export, allowing you to back up, reuse, modify, and share flowchart structures.

### Privacy

- All diagram data is stored locally.
- No data is transmitted to external servers.
- Flowchart information is stored as JSON inside Anki notes.
- Images are stored in Anki's media folder.
- Images are automatically referenced for compatibility with Anki exports and shared decks.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl + A` | Add Step / Box |
| `Ctrl + B` | Add Decision |
| `Ctrl + C` | Add Information |
| `Ctrl + Shift + E` | Edit selected element |
| `Ctrl + Shift + X` | Open Extra |
| `Ctrl + L` | Toggle Link Mode |
| `Ctrl + Shift + C` | Increment and apply Cloze |
| `Ctrl + Shift + Alt + C` | Apply current Cloze |
| `Ctrl + Shift + F` | Activate Focus Flow |
| `Ctrl + S` | Save to Anki note |
| `Ctrl + Z` | Undo |
| `Ctrl + Y` / `Ctrl + Shift + Z` | Redo |
| `Ctrl + +` / `Ctrl + -` | Zoom in / out |
| `Ctrl + 0` | Reset zoom |
| `Ctrl + 9` | Fit flowchart |
| `Ctrl + Mouse Wheel` | Zoom around cursor |
| `Delete` | Delete selected element or arrow |
| `Ctrl + Shift + Delete` | Clear flowchart |
| `Enter / F2` | Edit arrow label |
| `Escape` | Cancel Link Mode |

**Text formatting:** `Ctrl + B` Bold · `Ctrl + I` Italic · `Ctrl + U` Underline.

**Additional interactions:**
- Double-click an element to edit its text.
- Double-click an arrow to edit its label.
- Drag elements to reposition them.
- Drag blue connection points to connect elements.
- Use Shift + Click or Shift + Drag for multiple selection.
- Use Ctrl + V to paste images.

On macOS, use Command (⌘) instead of Ctrl for compatible shortcuts.

---

## 🚀 Installation

1. Download MEDFlow from the repository or its AnkiWeb add-on page.
2. Install the add-on in Anki.
3. Restart Anki.
4. The **MedFlow** note type will be created automatically.
5. Create a new note using this type.
6. Click the **Alg** button to open the editor.

---

## ⚙️ Compatibility

- Anki Desktop.
- Windows, macOS, and Linux.
- PyQt5 and PyQt6.
- Anki dark mode.
- Generated cards can be reviewed using compatible Anki clients, including AnkiMobile and AnkiWeb.

---

## 👥 Who Can Use MEDFlow?

MEDFlow is especially useful for:

- Medical students.
- Nursing students.
- Healthcare professionals.
- Students preparing for clinical examinations.
- Anyone who prefers visual learning and structured information.

Although designed with medical education in mind, MEDFlow can be used by anyone who enjoys creating and studying through flowcharts.

---

## 🤝 Acknowledgments & Development

MEDFlow was independently developed and inspired by the **ZeestMedical** project. We acknowledge and appreciate the original developers and contributors for their work.

AI tools were used throughout development to assist with programming, code generation, debugging, error identification, feature implementation, and user experience improvements.

The project's concept, direction, and development were independently conducted, with AI technologies serving as supporting tools.

---

**MEDFlow – Think Visually. Learn Actively. Remember More. 🧠✨**