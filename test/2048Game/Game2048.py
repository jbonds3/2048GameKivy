import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button

#1

#creates an instance of Game2048 widget class with given properties
class Game2048(Widget):
    pass

#creates instance of Game2048 Application
class Game2048App(App):

    # returns Game2048 widget as root element for apps UI
    # inits app
    def build(self):
        # root widget -> Game2048 widget
        return Game2048()

if __name__ == '__main__':
    Game2048App().run()
