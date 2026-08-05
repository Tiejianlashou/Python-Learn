# 注意:函数定义的时候并不会执行,只有在调用函数的时候,函数体的逻辑才会执行;函数必须先定义,后调用
# 函数定义
def out_line():
    print("--------------------------")
    print("--------------------------")

# 函数调用
out_line()


# 函数的参数与返回值
# 函数1: 计算圆的面积 -- 半径
def circle_area(r):
    area = 3.14 * r ** 2 # **代表平方
    return area

area = circle_area(10)
print(area)

# 函数2: 计算长方形的面积 -- 长, 宽
def rectangle_area(l,w):
    """
    根据长方形的长度和宽度, 计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l * w
    return area

print(rectangle_area(3,4))

# 函数3: 计算圆的面积,周长 -- 半径 -----> 如果返回值有多个,多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """
    根据圆的半径,计算圆的面积和周长
    :param r: 半径
    :return: 面积和周长
    """
    return 3.14 * r ** 2, 3.14 * 2 * r

al = circle_area_len(10)
print(al) # 这里输出结果是(314.0, 62.800000000000004)是因为存在精度的损失
print(type(al))

area, len = circle_area_len(10)
print(area)
print(len)

# 在这里,介绍一下内置函数round-->round(number,ndigits)-->number代表要四舍五入的数字,ndigits表示小数位的个数
def circle_area_len(r):
    return 3.14 * r ** 2, round(3.14 * 2 * r,1)

al = circle_area_len(10)
print(al)
print(type(al))



# 函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()

print("函数调用完毕 ~")
