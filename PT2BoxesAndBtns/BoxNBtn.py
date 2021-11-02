import kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App

class MyGridLayout(GridLayout):

    # **kwargs is used for keyworded variables to know
    # whjat their value is if x = 5
    # x called in the fxn is 5
    def __init__(self, **kwargs):
        #Call grid layout constructor
        # (GridLayout, self)
        # super.__init__ -> allows for multiple inheiritance which lets the child
        # class inherit features from one or more parent classes
        super().__init__(**kwargs)

        #set columns
        self.cols = 2

        #add wigdets
        self.add_widget(Label(text="Name: "))

        #Add input box
        self.name = TextInput(multiline = True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))

        #Add input box
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))

        #Add input box
        self.color = TextInput(multiline = False)
        self.add_widget(self.color)

        # submit btn
        self.submit = Button(text="Submit", font_size=32)

        #bind btn to an action
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'{name} is {pizza} is {color}')
        #print to screen
        self.add_widget(Label(text=f'{name} is {pizza} is {color}'))

        #clear input boxes
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyBox(App):
    def build(self):
        return MyGridLayout()

MyBox().run()
