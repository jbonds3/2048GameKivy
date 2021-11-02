import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class BtnSpan(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.topgrid = GridLayout()
        self.topgrid.cols = 2

        self.topgrid.add_widget(Label(text="Name"))

        self.topgrid.add_widget(TextInput(multiline = True))

        self.add_widget(self.topgrid)

        self.add_widget(Button(text="Submit"))


class MyBtnSpanApp(App):
    def build(self):
        return BtnSpan()

MyBtnSpanApp().run()
