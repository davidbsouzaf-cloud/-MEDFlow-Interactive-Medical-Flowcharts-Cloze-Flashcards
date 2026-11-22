
<h1>MEDFlow – Interactive Medical Flowcharts &amp; Cloze Flashcards</h1>

<p><strong>Transform complex medical concepts into interactive visual learning experiences.</strong></p>

<p>MEDFlow is an Anki add-on that allows you to create interactive medical flowcharts and transform them into Cloze flashcards. It combines visual organization, clinical reasoning, and Anki's spaced repetition system to make studying more active, structured, and engaging.</p>

<p>Inspired by the ZeestMedical project, MEDFlow was independently developed to provide an integrated flowchart editor directly within Anki.</p>

<hr>

<h2>MAIN FEATURES</h2>

<h3>1. Interactive Flowchart Editor</h3>

<p>Create medical algorithms using three types of elements:</p>

<ul>
<li><strong>Step / Box:</strong> Represents a procedure, clinical finding, stage, or piece of information.</li>
<li><strong>Decision:</strong> Represents a clinical decision or branching point, displayed as a diamond.</li>
<li><strong>Information:</strong> Highlights additional explanations and important details.</li>
</ul>

<p>Move, resize, and organize elements freely to create simple or complex clinical pathways.</p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/Imagen%20na%20parte%20da%20frente.gif" width="700"></p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/sele%C3%A7%C3%A3o%20de%20n%C3%B3s%2Bmudan%C3%A7a.gif" width="700"></p>

<p><strong>Additional features:</strong></p>

<ul>
<li>Automatic alignment guides.</li>
<li>Customizable colors, borders, and box appearance.</li>
<li>Multiple selection and simultaneous editing.</li>
<li>Change the type of multiple selected boxes at once.</li>
<li>Undo and redo functionality.</li>
<li>XMind-inspired keyboard shortcuts for faster diagram creation.</li>
</ul>

<h3>2. Connections &amp; Clinical Pathways</h3>

<p>Build relationships between elements using interactive connections.</p>

<ul>
<li>Connect elements using draggable blue connection points.</li>
<li>Create relationships between parent and child elements.</li>
<li>Reconnect arrows by dragging their endpoints.</li>
<li>Add labels such as Yes, No, Positive, Negative, or clinical criteria.</li>
<li>Build diagnostic and therapeutic decision trees.</li>
</ul>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/MUDAR%20SETAS.gif" width="700"></p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/bifurca%C3%A7%C3%A3o%20de%20setas.gif" width="700"></p>

<h3>3. Image Nodes</h3>

<p>Insert images directly into your flowcharts as independent visual elements.</p>

<p>Unlike images added to the Extra field, Image Nodes become part of the flowchart itself.</p>

<ul>
<li>Insert images directly into the editing area.</li>
<li>Paste copied images into the editor.</li>
<li>Freely resize and reposition images.</li>
<li>Connect images to other elements using arrows.</li>
<li>Add captions to images.</li>
<li>Display images directly in generated Anki cards.</li>
<li>Captions are automatically hidden when their corresponding images are hidden by Cloze.</li>
</ul>

<p>Ideal for anatomy, histology, radiology, pathology, dermatology, and other image-dependent medical subjects.</p>

<h3>4. Cloze Flashcard Generation</h3>

<p>Assign individual Cloze numbers to flowchart elements.</p>

<p>Elements sharing the same Cloze number belong to the same Anki card, while different numbers generate separate cards.</p>

<ul>
<li>Assign specific Cloze numbers or automatically increment numbering.</li>
<li>Display the complete flowchart during review.</li>
<li>Visually highlight the element being tested.</li>
<li>Reveal hidden elements by clicking them.</li>
<li>Review the complete flowchart or use Focus Flow to study specific branches.</li>
</ul>

<p>Use <strong>Save and Generate Cards</strong> to synchronize your flowchart with Anki and generate the corresponding Cloze cards.</p>

<h3>5. Focus Flow – Progressive Branch-Based Review</h3>

<p>Focus Flow provides a different way to review complex flowcharts by allowing you to study selected branches progressively.</p>

<p>Instead of displaying the entire algorithm at once, you can define a specific pathway and review its elements step by step.</p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/modo%20focus%20modo%20caixa%20pai.gif" width="700"></p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/focus%20sele%C3%A7%C3%A3o%20unica.gif" width="700"></p>

<p><strong>How it works:</strong></p>

<ul>
<li>Select the boxes belonging to a branch using Shift + Click or Shift + Drag.</li>
<li>Alternatively, select only the first box to automatically include its connected downstream elements.</li>
<li>Activate Focus using the target button or <code>Ctrl + Shift + F</code>.</li>
<li>Selected elements receive a visual Focus indicator.</li>
<li>During review, cards progressively follow the selected pathway, presenting one Cloze at a time.</li>
</ul>

<p><strong>During review:</strong></p>

<ul>
<li>The branch starts from its initial element.</li>
<li>Only the relevant pathway is displayed.</li>
<li>Arrows guide progression to the next step.</li>
<li>Unrelated branches remain hidden.</li>
<li>Elements without Cloze remain visible alongside related elements.</li>
<li>Cards without Focus settings continue displaying the complete flowchart.</li>
</ul>

<p>You can switch between the selected branch and the complete flowchart using the eye and target controls.</p>

<h3>6. Improved Mobile Review</h3>

<p>MEDFlow includes improvements designed to make complex flowcharts more readable on smaller screens, including AnkiMobile.</p>

<ul>
<li>Automatic adaptation to screen dimensions.</li>
<li>Prioritization of the active Cloze element.</li>
<li>Improved zoom and centering of relevant elements.</li>
<li>Option to fit the complete flowchart when necessary.</li>
<li>Adaptation to screen resizing and orientation changes.</li>
<li>Touch-friendly review controls.</li>
</ul>

<h3>7. Box Hints</h3>

<p>Add individual hints to flowchart elements without directly revealing their answers.</p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/dicas.gif" width="700"></p>

<ul>
<li>Add hints using the corresponding editor tool.</li>
<li>Hints appear in green above boxes in the editor.</li>
<li>During review, a <strong>+</strong> button appears when the corresponding box is hidden by Cloze.</li>
<li>Click the button to reveal the hint in place of the hidden content.</li>
<li>Click again to hide it.</li>
</ul>

<p>Ideal for clues, reminders, and information that supports active recall.</p>

<h3>8. Extra – Additional Content</h3>

<p>Attach explanations and complementary images to individual elements.</p>

<ul>
<li>Add clinical explanations and detailed notes.</li>
<li>Include observations and additional information.</li>
<li>Attach images to complementary content.</li>
<li>Display the corresponding Extra content during card review.</li>
</ul>

<p>Extra content appears on the back of the corresponding Cloze card.</p>

<h3>9. Templates – Ready-to-Use Flowchart Models</h3>

<p>Save time by starting with predefined flowchart structures instead of building every diagram from scratch.</p>

<p><img src="https://raw.githubusercontent.com/davidbsouzaf-cloud/-MEDFlow-Interactive-Medical-Flowcharts-Cloze-Flashcards/6c0c49f803104b610d165d8c676259ffe73aba8a/assets/criar%20templates.gif" width="700"></p>

<ul>
<li>Use predefined templates for medical subjects and clinical algorithms.</li>
<li>Save your own customized templates.</li>
<li>Save selected boxes or entire flowcharts as templates.</li>
<li>Reuse templates across different notes.</li>
<li>Restore the original templates when necessary.</li>
<li>Custom templates are stored separately from editor files, helping preserve them during add-on updates.</li>
</ul>

<h3>10. Undo &amp; Redo</h3>

<p>Edit with confidence using the editor's action history.</p>

<ul>
<li><code>Ctrl + Z</code> – Undo.</li>
<li><code>Ctrl + Y</code> or <code>Ctrl + Shift + Z</code> – Redo.</li>
<li>Restore previous box and arrow arrangements.</li>
<li>Maintain up to 200 editing states.</li>
</ul>

<h3>11. Text Formatting &amp; Visual Customization</h3>

<p>Customize content and appearance to improve organization and readability.</p>

<ul>
<li>Bold, italic, and underline.</li>
<li>Different font sizes and font families.</li>
<li>Bulleted and numbered lists.</li>
<li>Customizable box colors and borders.</li>
<li>Different arrow styles and colors.</li>
<li>Individual formatting for elements and connections.</li>
<li>Clear formatting options.</li>
</ul>

<h3>12. Import &amp; Export</h3>

<ul>
<li>Export flowcharts as JSON files.</li>
<li>Import previously exported diagrams.</li>
<li>Back up, reuse, and modify existing algorithms.</li>
<li>Share flowchart structures with other users.</li>
</ul>

<h3>13. Navigation &amp; Workspace</h3>

<ul>
<li>Zoom in, zoom out, and fit the entire flowchart to the workspace.</li>
<li>Pan across the canvas by dragging the background.</li>
<li>Zoom around the cursor using Ctrl + Mouse Wheel.</li>
<li>Automatically align elements using visual guides.</li>
<li>Select multiple elements using Shift + Click or Shift + Drag.</li>
<li>Collapse the sidebar for a cleaner workspace.</li>
<li>Dark mode compatibility.</li>
<li>Preserve zoom level and canvas position between the front and back of cards and between cards during the same review session.</li>
</ul>

<h3>14. Privacy &amp; Data Storage</h3>

<ul>
<li>No data is transmitted to external servers. Everything is stored locally on your computer.</li>
<li>Flowcharts are saved as JSON directly inside Anki notes, making backups, exports, and deck sharing easier.</li>
<li>Images are stored in Anki's media folder and automatically referenced, allowing them to be included in deck exports and shared decks.</li>
</ul>

<hr>

<h2>HOW TO USE MEDFLOW</h2>

<ol>
<li><strong>Install and open the editor:</strong> Install the add-on and restart Anki. The MedFlow note type is created automatically. Create a new note using this type and click <strong>Alg</strong> to open the editor.</li>
<li><strong>Build your flowchart:</strong> Add Step, Decision, and Information elements. Double-click an element to edit its text.</li>
<li><strong>Connect elements:</strong> Drag a blue connection point from one element to another, or use Link Mode.</li>
<li><strong>Assign Cloze numbers:</strong> Select an element and enter a number in the CLOZE field. Click Apply or use +1 to increment the number.</li>
<li><strong>Add images and Extra content:</strong> Insert Image Nodes directly into the flowchart or use Extra for complementary notes and images.</li>
<li><strong>Organize and customize:</strong> Use multiple selection, change box types, customize colors, add hints, and save frequently used structures as templates.</li>
<li><strong>Configure Focus Flow (optional):</strong> Select a branch using Shift + Click or Shift + Drag and activate Focus.</li>
<li><strong>Save and generate cards:</strong> Use Save to Card or Save and Generate Cards.</li>
</ol>

<p>Your cards are now ready for review!</p>

<hr>

<h2>KEYBOARD SHORTCUTS</h2>

<table>
<thead>
<tr><th>Shortcut</th><th>Action</th></tr>
</thead>
<tbody>
<tr><td><code>Ctrl + A</code></td><td>Add Step / Box</td></tr>
<tr><td><code>Ctrl + B</code></td><td>Add Decision</td></tr>
<tr><td><code>Ctrl + C</code></td><td>Add Information element</td></tr>
<tr><td><code>Ctrl + Shift + E</code></td><td>Edit selected element text</td></tr>
<tr><td><code>Ctrl + Shift + X</code></td><td>Open Extra</td></tr>
<tr><td><code>Ctrl + L</code></td><td>Toggle Link Mode</td></tr>
<tr><td><code>Ctrl + Shift + C</code></td><td>Increment and apply Cloze number</td></tr>
<tr><td><code>Ctrl + Shift + Alt + C</code></td><td>Apply current Cloze number</td></tr>
<tr><td><code>Ctrl + Shift + F</code></td><td>Activate Focus Flow</td></tr>
<tr><td><code>Ctrl + S</code></td><td>Save flowchart to Anki note</td></tr>
<tr><td><code>Ctrl + Z</code></td><td>Undo</td></tr>
<tr><td><code>Ctrl + Y</code> / <code>Ctrl + Shift + Z</code></td><td>Redo</td></tr>
<tr><td><code>Ctrl + +</code> / <code>Ctrl + -</code></td><td>Zoom in / out</td></tr>
<tr><td><code>Ctrl + 0</code></td><td>Reset zoom to 100%</td></tr>
<tr><td><code>Ctrl + 9</code></td><td>Fit entire flowchart</td></tr>
<tr><td><code>Ctrl + Mouse Wheel</code></td><td>Zoom around cursor</td></tr>
<tr><td><code>Delete</code></td><td>Delete selected element or arrow</td></tr>
<tr><td><code>Ctrl + Shift + Delete</code></td><td>Clear entire flowchart</td></tr>
<tr><td><code>Enter / F2</code></td><td>Edit selected arrow label</td></tr>
<tr><td><code>Escape</code></td><td>Cancel Link Mode</td></tr>
</tbody>
</table>

<p><strong>Text formatting:</strong> <code>Ctrl + B</code> Bold · <code>Ctrl + I</code> Italic · <code>Ctrl + U</code> Underline.</p>

<p><strong>Additional interactions:</strong></p>

<ul>
<li>Double-click an element to edit its text or an arrow to edit its label.</li>
<li>Drag elements to reposition them.</li>
<li>Drag the empty background to pan across the workspace.</li>
<li>Drag blue connection points to connect elements.</li>
<li>Use Shift + Click or Shift + Drag to select multiple boxes.</li>
<li>Use Ctrl + V to paste images into the editor or Extra.</li>
</ul>

<p>On macOS, use Command (⌘) instead of Ctrl for compatible shortcuts.</p>

<hr>

<h2>WHO IS MEDFLOW FOR?</h2>

<p>MEDFlow is designed for medical students, nursing students, healthcare professionals, and anyone who enjoys visual learning and wants to organize complex information using flowcharts.</p>

<p>It is particularly useful for:</p>

<ul>
<li>Diagnostic algorithms and differential diagnoses.</li>
<li>Therapeutic protocols and clinical guidelines.</li>
<li>Pathophysiology and disease progression.</li>
<li>Emergency medicine algorithms.</li>
<li>Clinical decision-making.</li>
<li>Anatomy, histology, pathology, and radiology.</li>
<li>Any subject that benefits from visual organization.</li>
</ul>

<p>You do not need to be a healthcare student or professional to use MEDFlow. Anyone who enjoys learning through flowcharts can benefit from it.</p>

<hr>

<h2>COMPATIBILITY</h2>

<ul>
<li>Anki Desktop.</li>
<li>Windows, macOS, and Linux.</li>
<li>PyQt5 and PyQt6 support.</li>
<li>Anki dark mode compatibility.</li>
<li>Generated cards can be reviewed in compatible Anki clients, including AnkiMobile and AnkiWeb.</li>
</ul>

<hr>

<h2>DEVELOPMENT, AI &amp; ACKNOWLEDGMENTS</h2>

<p>MEDFlow was independently developed, inspired by the ZeestMedical project. We acknowledge and appreciate the original developers and contributors for their work.</p>

<p>Artificial Intelligence (AI) tools were used throughout development to assist with programming, code generation, debugging, error identification, feature implementation, and user experience improvements.</p>

<p>The project's concept, direction, and development were independently conducted, with AI technologies serving as supporting tools throughout its creation.</p>

<hr>

<h2>MEDFlow – Think Visually. Learn Actively. Remember More. 🧠✨</h2>
