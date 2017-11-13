# -*- coding: UTF-8 -*-
# 算术运算符
a = 10 
b = 20

print a/b

print a*b

print b/a

print a%b

print a**b

print b/a

print b%a

#赋值运算符
a = 21
b = 10
c = 0

c += a
print "c 的值为：",c

c += a
print "2 - c 的值为：", c 

c *= a
print "c1 的值为：",c


#逻辑运算符 与，或，非

a = 10
b = 20

if (a and b):
    print "a 和 b 都为ture"
else:
    print "a 和 b 有一个不为true"

if (a or b):
    print "a 和 b 都为true,或其中一个变量为true"
else:
    print "变量a 和 b 都不为true"

#成员运算符
a = 10
b = 20
list = [1,2,3,4,5];

if (a in list):
    print "变量 a 在给定的列表 list 中"
else:
    print "变量 a 不在给定的列表 list 中"

if (b not in list):
    print "变量 b 不在给定的列表 list 中"
else:
    print "变量 b 在给定的列表 list 中"


#条件语句
name = 'Tinna'
if name == 'Tinna':
    print  "welcome boss, Tinna"
else:
    print  False




