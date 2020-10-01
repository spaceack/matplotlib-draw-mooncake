import numpy as np
from numpy import sin, cos
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

x = lambda d,r,R,theta: (R-r)*np.cos(theta) + d*np.cos(((R-r)/r)*theta)
y = lambda d,r,R,theta: (R-r)*np.sin(theta) - d*np.sin(((R-r)/r)*theta)
# 转数-内圆旋转次数
revs = 30
# 迭代次数， 即沿绘制路径获取的点。
Niter = 9999
thetas = np.linspace(0,revs*2*np.pi,num=Niter)

d = 10  #  距离
r = 46 # 小圆半径
R = 50 # 大圆半径
plt.plot(x(d, r, R, thetas), y(d, r, R, thetas))

d = 20  #  距离
r = 11 # 小圆半径
R = 12 # 大圆半径
plt.plot(x(d, r, R, thetas), y(d, r, R, thetas), color='orange', linewidth = '4')

length = 2.6
# 画个圆
theta = np.linspace(0, 2 * np.pi, 100)
x = length * cos(theta)
y = length * sin(theta)
plt.plot(x, y, color='orange', linewidth = '5')
length = 18
# 画个大圆
theta = np.linspace(0, 2 * np.pi, 100)
x = length * cos(theta)
y = length * sin(theta)
plt.plot(x, y, color='#FF6347', linewidth = '5')
plt.axis('equal')
plt.axis('off')

font_set = FontProperties(fname=r"Alibaba-PuHuiTi-Medium.ttf", size=12)
plt.text(-6, -6, '中秋\n快乐', bbox=dict(boxstyle='circle', fc="w", ec='orange', linewidth=4), fontproperties=font_set, fontsize=40, color='orange') ##ec为线条颜色，color为字体颜色,可以自由替换
plt.text(-20, -25, 'Python画月饼，千里共禅娟', fontproperties=font_set, fontsize=20, color='#aa4a30')

plt.show()