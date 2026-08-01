# # for循环: 遍历输入的字符串
#
#
# msg = input("请输入需要遍历的字符串: ")
#
# for s in msg:# s 表示遍历出来的元素 ;msg 表示需要遍历的数据
#     print(f"元素: {s}")
# else:
#     print("遍历结束!")
#
#
# '''
# range语句
# 作用:生成指定规则的数字序列
# 用法一:range(end) ->获取一个从0开始,到end结束的数字序列(不含end本身)
#   range(5)获取的数据就是0,1,2,3,4
# 用法二:range(start,end)->获取一个从start开始,到end结束的数字序列(不含end本身)
#   range(2,8)获取的数据就是2,3,4,5,6,7
# 用法3:range(start,end,step)->获取一个从start开始,到end结束的数字序列,step步长(不含end本身)
#   range(0,10,2)获取的数据就是0,2,4,6,8
# '''
# # 案例: 计算1-100之间所有奇数之和
# total = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i
# print("1-100之间的奇数累加之和:",total)
#
# #简化
# total = 0
# for i in range(1,101,2):
#     total += i
# print("1-100之间的奇数累加之和:",total)
#
#
# # 案例2: 计算 100-500 之间所有3的倍数的数字之和
# total = 0 #记录累加之和
#
# for i in range(102,501,3):
#     total += i
# print("100-500之间所有3的倍数的数字之和:",total)


'''
循环嵌套:根据输入的长方形的长度 m,宽度 n,打印一个长方形;
如下:是一个长度为10,宽度为5的长方形
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
'''
'''
print("*"):自带换行效果,每一次执行都会输出在新的一行中;
print("*",end=""):end表示的是每一次输出以什么结束;默认 \n,表示换行
'''
# 1. 接收键盘录入m,n
# 长度
m = int(input("请输入长方形的长度:"))
# 宽度
n = int(input("请输入长方形的宽度:"))

# 2.打印长方形
for i in range(n):
    for j in range(m):
        print("* ",end=" ")
    print()

# 案例 :打印99乘法表
# 自己写的
j = 1
for m in range(9):
    i=1
    for n in range (9):
        y=i*j
        if i <= j :
            print(f"{i} * {j} = {y}",end="  ")
            i+=1
    j+=1
    print("")
# 看博主写的
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {j*i}",end = "\t")#利用/t制表符更加整齐
    print()

'''
需求1 :根据输入的直角边的边长,打印等腰直角三角形(如下为直角边为5的等腰直角三角形)
*
* *
* * *
* * * *
* * * * *
'''
x = int(input ("请输入你要打印等腰直角三角形的边长: ")) # 边长
for i in range (1,x+1):
    for j in range (1,i+1):
        print("*",end="\t")
    print()



'''
需求2 :根据输入的数字,打印对应的数字金字塔(以下为6)
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6
'''
x = int (input("请输入需要打印数字金字塔对应的数字:"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end="\t")
    print()

'''
打印国际象棋棋盘(1代表白色,2代表黑色)
2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2
'''
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            print("2",end=" ")
        else:
            print("1",end=" ")
    print()


