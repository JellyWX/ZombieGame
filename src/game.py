from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock

from player import Player

class BG(Widget):
  r = NumericProperty(0.15)

class Game(Widget):

  ## game objects ##

  bg = ObjectProperty(None)
  player = ObjectProperty(None)

  ## rendering stuff ##

  aspect_x = 16.0/9
  aspect_y = 9.0/16

  proper_w = 160
  proper_h = 90

  ## useful things ##

  started = 1

  mouse_pos = (0,0)
  keysdown = set([])

  def __init__(self,*args,**kwargs):
    super(Game,self).__init__(*args,**kwargs)
    Builder.load_file('game.kv') ## load the game's assigned layout file ##

    Clock.schedule_interval(self.update,1.0/40)

  def catch_mouse(self,etype,pos):
    self.mouse_pos = pos

  def keyDown(self,window,key,*largs):
    self.keysdown.add(key)

  def keyUp(self,window,key,*largs):
    self.keysdown.remove(key)

  def on_touch_down(self,mouse):
    pass

  def update(self,t):
    self.player.resetVel()
    if 119 in self.keysdown:
      self.player.up()

    if 115 in self.keysdown:
      self.player.down()

    if 97 in self.keysdown:
      self.player.left()

    if 100 in self.keysdown:
      self.player.right()

    self.player.move()

    if float(self.width) / self.height < self.aspect_x:
      self.proper_w = self.width
      self.proper_h = self.width * self.aspect_y

    elif float(self.width) / self.height > self.aspect_x:
      self.proper_w = self.height * self.aspect_x
      self.proper_h = self.height

    if self.started:
      self.size_widgets()

  def size_widgets(self):
    self.player.size = self.proper_w/64,self.proper_h/64
    #self.player.center = self.center_x + self.player.map_x,self.center_y + self.player.map_y

    self.bg.size = self.proper_w,self.proper_h
    self.bg.center = self.center
    self.bg.r = self.proper_h * 1 / 100
