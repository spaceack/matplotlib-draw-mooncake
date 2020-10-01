import numpy as np
from numpy import sin, cos
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

x = lambda d,r,R,theta: (R-r)*np.cos(theta) + d*np.cos(((R-r)/r)*theta)
y = lambda d,r,R,theta: (R-r)*np.sin(theta) - d*np.sin(((R-r)/r)*theta)
# 转数-内圆旋转次数
revs = 888
# 迭代次数， 即沿绘制路径获取的点。
Niter = 2024
thetas = np.linspace(0,revs*2*np.pi,num=Niter)

d = 8  #  距离
r = 36 # 小圆半径
R = 35 # 大圆半径
plt.plot(x(d, r, R, thetas), y(d, r, R, thetas), color='orange')

length = 7
# 画个圆
theta = np.linspace(0, 2 * np.pi, 100)
x = length * cos(theta)
y = length * sin(theta)
plt.plot(x, y, color='orange', linewidth = '5')

font_set = FontProperties(fname=r"Alibaba-PuHuiTi-Medium.ttf", size=12)
plt.text(-1.5, -1, '中秋', bbox=dict(boxstyle='circle', fc="w", ec='orange', linewidth=4), fontproperties=font_set, fontsize=40, color='orange') ##ec为线条颜色，color为字体颜色,可以自由替换
plt.axis('off')

plt.show()