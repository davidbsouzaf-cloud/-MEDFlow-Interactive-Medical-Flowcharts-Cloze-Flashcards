MedFlow - Image captions, box hints, Focus flow and box selection

1) Image caption
Every image box has a caption space inside its own frame, right below the picture. Click it and type; Enter or Esc confirms, and the box grows downwards if the text needs more lines. On the cards the caption shows under the picture in the same frame; images without caption text show just the picture (no empty strip). Images created before this version get the caption space once, when the editor opens them (the box grows downwards, the picture keeps its size). Resizing the picture keeps the picture's proportions and the caption strip's height.

Arrow style menu: the four arrow icons are now centered inside their buttons (they were piled up at the top of the menu).

2) Box hints
Each box has a + on its top-left corner in the editor (visible on hover / when selected). Click it (or press Ctrl+Shift+H): a small box opens next to the box. Type the hint and press OK (or Enter; Shift+Enter = new line, Esc = cancel). The hint then stays written in green above the box, on its top-left corner, and the + is replaced by it. Click the green text to edit it; saving it empty removes the hint.
If several boxes are selected and you write the hint on one of them, it is applied to all the selected boxes (leaving it empty removes it from all of them).
In the review there is nothing to click: when a box is the hidden cloze and has a hint, the hint is already shown in the middle of the box, in place of [...]. Click the box to reveal the answer as usual.
The green "extra" badge is at the bottom-left corner of the box.

3) Focus flow (the chart is built arrow by arrow)
Select the boxes of a branch (Shift+drag, or Shift+click) - e.g. A, B and C - and click the Focus button (sidebar, target icon) or press Ctrl+Shift+F. Those boxes get a "focus" badge. If you select just the first box of the branch, it is marked together with everything that hangs from it. Selecting marked boxes and clicking Focus again removes the group.
In the review, when the asked cloze belongs to a focus group, the card starts from the box the group hangs from (e.g. the disease) and only the arrow into the first box is drawn, with that box hidden as a cloze. After you answer it, the next card draws the arrow to the next box, and so on. Boxes without a cloze appear together with their parent. The rest of the chart (other branches) is omitted.
Cards whose cloze is outside every focus group show the whole flowchart.
On the card, the eye button (zoom bar) shows the whole flowchart temporarily; the target button brings the focus back. The next card starts focused again.

4) Box selection (lilac)
Hold Shift and drag on the empty background: everything the rectangle touches is selected while you drag (boxes, and the arrows that pass through it), with a counter on the rectangle. Add Ctrl to keep the current selection. Shift+click on boxes / arrows adds or removes them.
Anything selected with Shift or with the drag rectangle is shown in lilac. While boxes are lilac, clicking a shape button (step, decision, information) turns those boxes into that shape instead of adding a new one (image boxes are left as they are). A normal click selects a single box in the usual blue and the buttons add boxes as before.

5) Layout changes
- The text formatting bar (size, font, B / I / U, lists, clear) is now part of the top toolbar, where the cloze numbering used to be.
- The cloze numbering (CLOZE #, Apply, +1) moved to the bottom bar, at the left of Close / Save. Enter in the number field applies it.
- Arrowheads are centred on the line: curved arrows now end with a short straight run under the head (and elbow arrows keep a longer last segment), instead of the line entering one corner of the head.
Install: also replace __init__.py with the one in this package.
