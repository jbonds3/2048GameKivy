# design file
#import not neede becuase theyre described in kv file
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class TheApp2(Widget):

    #none -> when the app starts variable wont have value
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        pizza = self.pizza.text
        color = self.color.text

        print(f'My pizza is {pizza}, fav color is {color}')

        pizza = ''
        color = ''

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

        return TheApp()

#kivy file needs the same name before the App part lowercase
#i.e. JohnApp(App) -> john.kv
class MyApp(App):
    def build(self):
        return TheApp()

if __name__ == '__main__':
    MyApp().run()
