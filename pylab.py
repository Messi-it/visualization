from pylab import *

x = arange(0,10,1)
y = randn(len(x))
# randn是一个产生正态分布函数数字或矩阵的函数
plot(x,y)

title = ('pylab')
show()