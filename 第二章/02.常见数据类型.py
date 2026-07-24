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
     大家记得好好学习哦 ~ 
""" #三引号定义(多行字符串)

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

#定义字符串 ---> It's very good
#转义字符 \' \" \n \t
msg1 = "It\'s very good"
print(msg1)

msg2 = "It's very good"
print(msg2)

msg3 = "Hello的意思就是\"您好\""
print(msg3)

msg4 = 'Hello的意思就是"您好"'
print(msg4)

print("\t欢迎大家进入到Python课程的学习!\n\t大家记得一键三连哦 ~ ")#\n --> 换行;\t --> 缩进


# 字符串的拼接
s1="人生苦短""我用Python"",OK"
print(s1)

msg1 = "人生苦短"
msg2 = "我用Python"
print("猪猪侠说:" + msg1 + "," + msg2)

# 案例:---> str(int数字) ---> 将int类型的数字转为字符串
name = "猪猪侠"
age = 18
pro = "信息安全"
hobby = "Python和Java"
print("大家好,我是" + name + ",今年" +str(age) + "岁,学习的专业是" + pro + ",爱好" + hobby)

#字符串格式化 --> 方式一 : %s 占位符
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s" %(name, age, pro, hobby))

#字符串格式化 --> 方式二 : f"..{变量名/表达式}" ----->推荐使用这种方式
name = "猪猪侠"
age = 18
pro = "信息安全"
hobby = "Python和Java"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")