import kivy
kivy.require('1.2.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Phone(Widget):
	ti = ObjectProperty(None)
	lastOp = ""
	memorynum = 0.0
	operation = False

	def _execute(self, op):
		if op in "0123456789*#":

			self._setText(op)
		elif op == "Delete":
			self.ti.text = self.ti.text[:-1]

	def _setText(self, op):
		if self.operation:
			self.ti.text = op
			self.operation = False
		else:
			self.ti.text += op

class PhoneApp(App):
	use_kivy_settings = False
	def build(self):
		self.Calc = Phone()
		return self.Calc



if __name__=='__main__':
	Ap = PhoneApp()
	Ap.run()
