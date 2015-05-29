# -*- coding:utf-8 -*-


import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



"""
particleクラスを実装する。
位置、速度、位置更新関数を用意する。
"""


class Particle:
	def __init__(self,name,pos_x,pos_y,velocity_x,velocity_y):
		self.name = name
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.velocity_y = velocity_y
		self.velocity_x = velocity_x

class sample(Particle):
	def __init__(self,math,*av):
		Particle.__init__(self,*av)
		self.math = math

	def move(self,t):
		if 0 < self.pos_y + self.velocity_y * t < 200:
			self.pos_y = self.pos_y + self.velocity_y * t
		else:
			self.pos_y = self.pos_y - self.velocity_y * t
			self.velocity_y = -1 * self.velocity_y

		if 0 < self.pos_x + self.velocity_x * t < 200:
			self.pos_x = self.pos_x + self.velocity_x * t
		else:
			self.pos_x = self.pos_x - self.velocity_x * t
			self.velocity_x = -1 * self.velocity_x

	def getPositionX(self):
		return self.pos_x

	def getPositionY(self):
		return self.pos_y

particles = []
for i in range(100):
	particles.append(sample(i,i,random.randint(1, 199),random.randint(1, 199),random.randint(1, 10),random.randint(1, 10)))

fig = plt.figure()

frame_list = []

for i in range(500):
	x = []
	y = []
	for elem in particles:
		elem.move(0.1)
		x.append(elem.getPositionX())
		y.append(elem.getPositionY())
	one_frame = plt.plot(x, y,'o')
	frame_list.append(one_frame)

ani = animation.ArtistAnimation(fig, frame_list, interval= 40, repeat_delay=1)
plt.show()

"""
アニメーションは何かの変化を表現できるということで、今回は、正規分布 と ポアソン分布 のパラメータを離散的に推移させて、グラフの概形がどのように移り変わるかを 可視化 してみた。
"""