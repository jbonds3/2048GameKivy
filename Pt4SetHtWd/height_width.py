import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyHTWD1(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.top_gridlayout = GridLayout()
        self.top_gridlayout.cols = 2
        self.add_widget(self.top_gridlayout)


        self.lname = Label(text='Name: ')
        self.top_gridlayout.add_widget(self.lname)

        self.tiname = TextInput(multiline = True)
        self.top_gridlayout.add_widget(self.tiname)


        self.cols = 1

        self.submit = Button(text = 'Submit',
            font_size = 32,
            # y = height, disable the widget being the size of the container it's in
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
            )
        self.add_widget(self.submit)

class MyHTWD2(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # changes the properties of the main GridLayout
        self.row_force_default=True
        self.row_default_height=40
        self.col_force_default=True
        self.col_default_width=100

        # changes the height and width of this gridlayout widget
        self.top_gridlayout = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
            )

        self.top_gridlayout.cols = 2
        self.add_widget(self.top_gridlayout)


        self.lname = Label(text='Name: ')
        self.top_gridlayout.add_widget(self.lname)

        self.tiname = TextInput(multiline = True)
        self.top_gridlayout.add_widget(self.tiname)


        self.cols = 1

        self.submit = Button(text = 'Submit',
            font_size = 32,
            # y = height, disable the widget being the size of the container it's in
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
            )
        self.add_widget(self.submit)

class MyHTWDApp(App):
    def build(self):
        return MyHTWD2()

if __name__ == '__main__':
    MyHTWDApp().run()
