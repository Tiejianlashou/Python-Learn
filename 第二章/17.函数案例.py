# 案例1: 定义一个函数: 根据传入的底和高计算三角形面积的函数 (三角形面积 = 底 * 高 / 2).
from _testcapi import awaitType


def triangle_area(b,h):
    """
    计算三角形的面积
    :param b: 底
    :param h: 高
    :return: 三角形的面积
    """
    return b*h/2

print("底长为 3 ,高为 10 的三角形的面积 : ",triangle_area(3,10))
# 案例2: 定义一个函数: 计算传入的字符串中元音字母的个数 (元音字母为aeiouAEIOU).
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for i in s:
        if i in "aeiouAEIOU" :
            num += 1
    return num

print(count_aeiou("Hello Python Hello World"))
# 案例3: 定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分(保留1位小数),并返回.
def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分,最低分,平均分
    :param score_list: 分数列表
    :return: 最高分,最低分,平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list),1)
    return max_s,min_s,avg_s

s_list = [589,609,605,643,677,455,477,489,503]
max_score,min_score,avg_score = calc_score(s_list)
print("最高分:",max_score)
print("最低分:",min_score)
print("平均分:",avg_score)



"""
 练习1 : 定义一个函数,根据传入的分数,计算对应的分数等级并返回
 分数 >= 90 : A
 分数 >= 75 : B
 分数 >= 60 : C
 分数 < 60 : D
"""
def grade(score):
    """
    定义一个函数,根据传入的分数,计算对应的分数等级并返回
    :param score: 成绩
    :return: 成绩等级
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

print("您的成绩等级为:",grade(90))

"""
练习2:
定义一个函数,用于判断一个字符串是否是回文串,返回bool值
把字符串反转,如果与原字符串相同,就是回文串(例如:"level","radar","黄山落叶松叶落山黄")
"""
def s_huiwen(s):
    """
    判断是否为回文串
    :param s: 传入的字符串
    :return: bool值,True代表是回文串,False代表不是
    """
    print(s[::-1]==s)
s_huiwen("level")

"""
练习3:
定义一个函数,完成时间转换功能,将传入的秒转换成小时,分钟,秒
"""
def transform_clock(t):
    """
    将输入的秒转换为小时,分钟,秒
    :param t: 需要转换的秒数
    :return: 打印转换后的时间
    """
    hour = t // 3600
    a = t % 3600
    min = a // 60
    second = a % 60
    return(print(f"{t}秒转换为{hour}时{min}分{second}秒"))
clock = int(input("请输入你要转换的秒数:"))
transform_clock(clock)

"""
定义一个函数:根据传入的三角形三个边的边长,判定三角形的类型(等边,等腰,普通,或者不能构成三角形)
"""
def judge_triangle(a,b,c):
    """
    判断三角形类型
    :param a: 边长
    :param b: 边长
    :param c: 边长
    :return: 没有返回值
    """
    if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0:
        if a == b == c:
            print(f"{a},{b},{c}构成等边三角形")
        elif a==b or b==c or a==c:
            print(f"{a},{b},{c}构成等腰三角形")
        else:
            print(f"{a},{b},{c}构成普通三角形")
    else :
        print(f"{a},{b},{c}不能构成三角形")
    return 0
a = float(input("请输入你要判断的第一条边长:"))
b = float(input("请输入你要判断的第二条边长:"))
c = float(input("请输入你要判断的第三条边长:"))
judge_triangle(a,b,c)

# 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。#这是官方答案
def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "等边三角形"
        elif a == b or a == c or b == c:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"


print(triangle_type(3, 4, 5))
print(triangle_type(3, 3, 5))
print(triangle_type(3, 4, 6))
print(triangle_type(3, 5, 6))
print(triangle_type(3, 4, 7))
print(triangle_type(8, 8, 8))