import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button

#1

#creates an instance of Name widget class with given properties
class Name(Widget):
    pass

#creates instance of Name Application
class NameApp(App):

    # returns Name widget as root element for apps UI
    # inits app
    def build(self):
        # root widget -> Name widget
        return Name()
#2

class NamesApp(App):
    def build(self):
        return Button(text='John Bonds III')

while 1:

    print('Enter which name display example 1 or 2: ', end='')
    userOption = input()

    if userOption == '1':
        NameApp().run()
    elif userOption == '2':
        NamesApp().run()
