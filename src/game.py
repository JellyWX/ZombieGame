from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock

from player import Player
from locations import ASSETS

class BG(Widget):
  r = NumericProperty(0.15)

class Tree(Widget):
  source = '{}/untiled/test_tree.png'.format(ASSETS)

class Game(Widget):

  ## game objects ##

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

    self.tree = Tree()
    self.tree.o_xs = 'self.center_x / 2'
    self.tree.o_ys = 'self.center_y / 2'
    self.add_widget(self.tree)

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


    children_sorted = sorted(self.children,key=lambda w: w.y)
    children_sorted.reverse()

    for i in children_sorted:
      if type(i) != BG:
        self.remove_widget(i)
        self.add_widget(i)

    self.size_widgets()

  def size_widgets(self):
    for i in self.children:
      if type(i) not in [BG,Player]:
        i.o_x = eval(i.o_xs)
        i.o_y = eval(i.o_ys)
        i.pos = i.o_x - self.player.map_x,i.o_y - self.player.map_y

        if i.y < self.player.y:
          i.opacity = 0.5

        else:
          i.opacity = 1

    self.player.size = self.proper_w/64,self.proper_h/64
    self.player.center = self.center
