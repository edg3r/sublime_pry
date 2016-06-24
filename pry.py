import sublime, sublime_plugin

class PryCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, self.view.sel()[0].a, "require 'pry';binding.pry")
