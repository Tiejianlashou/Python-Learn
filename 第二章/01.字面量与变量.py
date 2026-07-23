#字面量的写法

print(100) # 整数(int)
print(3.14) # 浮点型/小数(float)
print(True) # 布尔(bool)
print(False) # 布尔(bool)
print("Hello Python") # 字符串(str)
print("---------------") # 字符串(str)
print(None) # 空值(NoneType)

#布尔类型本质也是整数类型(True为 1 ; False为 0)
print(True + 1)
print(False - 1)

#变量 ----> Python是动态类型语言,一个变量是可以存储不同类型的数据的(但是项目开发中,推荐变量只存储一种类型的数据)
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)

#案例 :
base = 20.7
incr = 50
print("第一个月播放总量:",base+incr)
print("第二个月播放总量:",base+incr*2)

#或者可以一次性可以定义多个变量
base,incr = 20.7,50
print("第一个月播放总量:",base+incr)
print("第二个月播放总量:",base+incr*2)


#案例 : 现在有两个变量,分别为: a = 10, b = 20,现需要将这两个变量值交换,然后输出到控制台
a,b = 10,20
c = a
a = b
b = c
print(a,b)

#案例 : 现有三个变量,分别为: a = 100, b = 200, c = 300 ,现需要将这三个变量值进行交换,将a,b,c的值分别赋值给c,a,b,并将其输出到控制台
a,b,c = 100,200,300
#c -> b -> a -> c
d = c
c = a
a = b
b = d
print( c,a,b )






