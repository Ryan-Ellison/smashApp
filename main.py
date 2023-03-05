# import module
import numpy as np
import kivy
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

kivy.require('2.1.0')


class CharacterScreen(GridLayout):

    def __init__(self, **kwargs):
        super(CharacterScreen, self).__init__(**kwargs)
        self.cols = 5
        #for x in charactersList:
        #    self.add_widget(Label(text=x))
        for count in range(20):
            self.add_widget(CustomBtn(count))


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])

    def __init__(self, count):
        super().__init__()
        self.count = count
        text: 'press me'

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print('pressed {count} at {pos}'.format(count=self.count, pos=pos))

class MyApp(App):
    def build(self):
        return CharacterScreen()


if __name__ == '__main__':
    charactersList = np.array(open("Characters.txt", "r").read().splitlines())
    MyApp().run()
