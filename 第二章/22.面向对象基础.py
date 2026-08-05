#定义类-----> 不推荐 动态的对象添加属性
class Car:
    pass

#创建对象
c1 = Car()
#动态的对象添加属性
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000

print(c1)
print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出出来
print(c1.brand)


# 定义类
class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕,对象属性已经添加完毕 .")


#创建对象
c1 = Car("红色","BMW","X5",50000)
print(c1.color)
print(c1.__dict__)