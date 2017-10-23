from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from math import sqrt

class Player(Widget):
  map_x = NumericProperty(0)
  map_y = NumericProperty(0)

  map_pos = ReferenceListProperty(map_x,map_y)

  vel_x = NumericProperty(0)
  vel_y = NumericProperty(0)

  vel = ReferenceListProperty(vel_x,vel_y)

  inventory = []

  def up(self):
    self.vel_y = 1

  def down(self):
    self.vel_y = -1

  def right(self):
    self.vel_x = 1

  def left(self):
    self.vel_x = -1

  def resetVel(self):
    self.vel_x = 0
    self.vel_y = 0

  def move(self):
    self.map_pos = (Vector(self.vel).normalize())*2 + self.map_pos
