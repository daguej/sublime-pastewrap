import sublime, sublime_plugin

class PasteWrapCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# get contents of the clipboard
		clipboard = sublime.get_clipboard()
		view = self.view

		for region in view.sel():
			if not region.empty():
				s = view.substr(region)
				s = clipboard.replace("*", s)
				view.replace(edit, region, s)
