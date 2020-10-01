import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

x = lambda d,r,R,theta: (R-r)*np.cos(theta) + d*np.cos(((R-r)/r)*theta)
y = lambda d,r,R,theta: (R-r)*np.sin(theta) - d*np.sin(((R-r)/r)*theta)
# 转数-内圆旋转次数
revs = 800
# 迭代次数， 即沿绘制路径获取的点。
Niter = 99999
thetas = np.linspace(0,revs*2*np.pi,num=Niter)
d = 20
r = 23
R = 60
plt.plot(x(d, r, R, thetas), y(d, r, R, thetas), color='orange', linewidth = '4')
plt.axis('equal')
plt.axis('off')
font_set = FontProperties(fname=r"Alibaba-PuHuiTi-Medium.ttf", size=12)
plt.text(-16, -15, '中秋\n快乐', bbox=dict(boxstyle='circle', fc="w", ec='orange', linewidth=4), fontproperties=font_set, fontsize=40, color='orange') ##ec为线条颜色，color为字体颜色,可以自由替换
plt.text(-2, -70, 'Python做月饼，千里共禅娟', fontproperties=font_set, fontsize=20, color='#aa4a30')
plt.show()