from kivy.uix.widget import Widget
from kivy.properties import BoundedNumericProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from math import sqrt

class Player(Widget):
  map_x = NumericProperty(0)
  map_y = NumericProperty(0)

  map_pos = ReferenceListProperty(map_x,map_y)

  off_x = NumericProperty(0)
  off_y = NumericProperty(0)

  off_pos = ReferenceListProperty(off_x,off_y)

  buffer_x = BoundedNumericProperty(0,min=-100,max=100)
  buffer_y = BoundedNumericProperty(0,min=-100,max=100)

  buffer_pos = ReferenceListProperty(buffer_x,buffer_y)

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
    try:
      self.buffer_pos = Vector(self.vel).normalize() + self.buffer_pos
      self.off_pos = Vector(self.vel).normalize() + self.off_pos
    except ValueError:
      self.off_pos = Vector(self.vel).normalize()*2 + self.off_pos

    self.map_pos = Vector(self.vel).normalize()*2 + self.map_pos
