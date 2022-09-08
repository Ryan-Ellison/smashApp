# import module
import numpy as np
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
kivy.require('2.1.0')


class CharacterScreen(GridLayout):

    def __init__(self, **kwargs):
        super(CharacterScreen, self).__init__(**kwargs)
        self.cols = 5
        for x in charactersList:
            self.add_widget(Label(text=x))

class MyApp(App):
    def build(self):
        return CharacterScreen()


if __name__ == '__main__':
    charactersList = np.array(open("Characters.txt", "r").read().splitlines())
    MyApp().run()
