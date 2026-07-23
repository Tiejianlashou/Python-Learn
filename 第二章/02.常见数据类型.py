#常见数据类型
print("Hello")
print(type("Hello")) # str

print(type(10)) # int
print(type(3.14)) # float
print(type(True)) # bool
print(type(False)) # bool
print(type(None)) # NoneType

num = -100
print(type(num)) # int

#常见数据类型 ---> isinstance(数据,类型) --> bool值 --> 判定数据是否是指定的类型,如果是: True,否则: False
print(isinstance(num, int))
print(isinstance(num,float))
print(isinstance(num,bool))

# 字符串
# 定义字符串的三种方式
s1 = "Hello" # 双引号定义
s2 = 'Python' # 单引号定义
s3 = """
Hello:
     欢迎大家进入到Python课程的学习!

"""
