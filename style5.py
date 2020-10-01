import numpy as np
from numpy import sin, cos
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

X = []
Y = []
x = lambda d,r,R,theta: (R-r)*np.cos(theta) + d*np.cos(((R-r)/r)*theta)
y = lambda d,r,R,theta: (R-r)*np.sin(theta) - d*np.sin(((R-r)/r)*theta)
# 转数-内圆旋转次数
revs = 88
# 迭代次数， 即沿绘制路径获取的点。
Niter = 200
thetas = np.linspace(0,revs*2*np.pi,num=Niter)
d = 2  #  距离
r = 6 # 小圆半径
R = 3 # 大圆半径
plt.plot(x(d, r, R, thetas), y(d, r, R, thetas), color='orange', linewidth = '4')

font_set = FontProperties(fname=r"Alibaba-PuHuiTi-Medium.ttf", size=12)
plt.axis('off')

plt.show()