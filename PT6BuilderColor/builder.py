# design file
#import not needed because theyre described in kv file
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#helps src file import widget from specific kv file
Builder.load_file('whatever.kv')

class TheApp(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'My name is {name}, pizza is {pizza}, fav color is {color}')

        name = ''
        pizza = ''
        color = ''

#kivy file needs the same name before the App part lowercase
#i.e. JohnApp(App) -> john.kv
class AweApp(App):
    def build(self):
        return TheApp()

if __name__ == '__main__':
    AweApp().run()
