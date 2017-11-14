#coding=utf-8

numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) >0 :
    number = numbers.pop()
    if (number % 2 ==0):
        even.append(number)
    else:
        odd.append(number)
print even
print odd


count = 0
while count < 9:
    print "count 的值是", count
    count = count + 1
print "Good bye"


#continue
i = 1
while i < 10:
    i += 1
    if i%2>0:
        continue
    print i



#break
i = 1
while 1:
    print i
    i += 1
    if i >10:
        break




#无限循环
#var = 1
#while var == 1:  # 该条件永远为true，循环将无限执行下去
#    num = raw_input("Enter a number :")
#    print "You entered :", num

#print "Good bye!"


#while 循环中使用else

count = 0
while count < 5:
    print count, "is less than 5"
    count = count + 1
else:
    print count,"is not less than 5"
    