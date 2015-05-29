# -*- coding:utf-8 -*-
import math, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
data_list = []

tmp = range(0, 200)
sigma_list = map(lambda x: x*0.01, tmp)
print sigma_list
mu_list = np.tile(0, len(sigma_list))
frame_list = []

x = np.arange(-5., 5., 0.001)
for v in zip(sigma_list, mu_list):
    y = (1./np.sqrt(2*np.pi*v[0]) * np.exp(-(x-v[1])**2/2/v[0]))
    one_frame = plt.plot(x, y)
    frame_list.append(one_frame)

ani = animation.ArtistAnimation(fig, frame_list, interval= 40, repeat_delay=1)
plt.show()

"""
アニメーションは何かの変化を表現できるということで、今回は、正規分布 と ポアソン分布 のパラメータを離散的に推移させて、グラフの概形がどのように移り変わるかを 可視化 してみた。
"""