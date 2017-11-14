#for 循环

for letter in "Python":
    print "当前字母:",letter


fruits = ['banana','apple','orange']
for fruit in fruits:
    print "当前水果:",fruit

print "Good Bye!"

#使用索引
fruits = ['banana','apple','orange']
for index in range(len(fruits)):
    print "当前水果:",fruits[index]

print "Good Bye!"
#以上实例使用了内置函数len()和range(),函数len()返回列表的长度，即元素的个数。range返回一个序列的数。


#for 循环使用else
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
#看不懂这个
