#coding=utf-8
#for 循环生成list
L=[]
for x in range(1,11):
    L.append(x*x)
print L

#列表生成器
s = [x*x for x in range(1,11)]
print s

v = [x*x for x in range(1,11) if x % 2 == 1]
print v

import os
a = [d for d in os.listdir('.')]
print a

d = {'x':'a','y':'b','z':'c'}
n = [k +'='+ v for k,v in d.iteritems()]
print n