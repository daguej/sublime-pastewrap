About
=====

PasteWrap wraps your current selection(s) with whatever is on the clipboard.

It does this by replacing the asterisk `*` in the clipboard contents with the contents of your selection.

Example
=======

Copy some text to the clipboard normally:

    <div class="i dont want to repeat myself">*</div>

Then select stuff in sublime.

    <p>I want to wrap this element!</p>

Press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd> and watch the magic happen.

    <div class="i dont want to repeat myself"><p>I want to wrap this element!</p></div>