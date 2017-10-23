from kivy.app import App
from kivy.base import EventLoop
from kivy.core.window import Window

from screenmanager import Manager

class Main(App):

  def on_start(self):
    Window.bind(on_key_down=self.manager.game.keyDown,on_key_up=self.manager.game.keyUp,mouse_pos=self.manager.game.catch_mouse)

  def build(self):
    self.manager = Manager()
    return self.manager

zg = Main()
