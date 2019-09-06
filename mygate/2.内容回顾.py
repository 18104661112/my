# 继承 多态 封装
# property classmethod staticmethod

# 封装
# 面向对象的语言本身就具有封装的特性 : 属性和方法都放在它所属的类中
# 私有化 :
    # __名字
        # 静态属性\对象属性
        # 方法
            # 私有的方法
            # 私有的类方法
            # 私有的静态方法
    # 如何实现的
        # 通过在类的内部定义或者使用的时候会自动添加_类名来进行变形
        # 在类的外部使用的时候由于python不会做自动的变形,所以这个属性就被隐藏了
        # 如果我们一定要在外部使用,也可以自己加上_类名的变形机制
        # 但十分不建议你在类的外部直接使用私有的名字
    # 私有的
        # 不能在类的外部使用
        # 也不能被继承

# class A:
#     @classmethod
#     def __func(cls):
#         print('infunc')
#
#     @classmethod
#     def f(cls):
#         cls.__func()
#
#
# print(A.f)

# class A:
#     @staticmethod
#     def __func():
#         print('infunc')
#
#     @classmethod
#     def f(cls):
#         cls.__func()
#
# A.f()

# property 把一个方法变成一个属性
# class Circle:
#   @property
#   def area(self):
#       pass

# c.area()
# c.area          # get 获取某个值
# c.area = 1      # set 给某一个属性赋值
# del c.area      # delete 删某个属性

# class Box:   # 盒子
#     def __init__(self,length,width,height):
#         self.__len = length
#         self.__width = width
#         self.__height = height
#
#     @property
#     def len(self):
#         return self.__len
#
#     @len.setter
#     def len(self,value):
#         if type(value) is int or type(value) is float:
#             self.__len = value
#
#     @len.deleter
#     def len(self):
#         del self.__len


# 盒子 = Box(10,20,30)
# ret = 盒子.len
# print(ret)
#
# 盒子.len = 'aaaa'
# ret = 盒子.len
# print(ret)
#
# del 盒子.len


# 1.基础的方法和语法能不能记住 :
    # 基础的数据类型 函数(内置函数\匿名函数的语法\普通函数)
    # 面向对象的基础语法 定义类 实例化 对象使用方法 查看属性
    # 继承的语法 多态的概念 封装的语法
    # 几个装饰器 :对应的功能,方法长什么样
# 2.基础的需求能不能完成
# 3.进阶的知识点 : 装饰器 生成器 递归函数 各种知识点的活学活用


# class File:   # 盒子
#     def __init__(self,path):
#         self.__path = path
#
#     @property
#     def f(self):
#         self.__f = open(self.__path,mode='w',encoding='utf-8')
#         return self.__f
#
#     @f.deleter
#     def f(self):
#         self.__f.close()
#         del self.__f
#
#
# obj = File()
# obj.f # 文件句柄
# obj.f.write('balabala')
# del obj.f


# classmethod
# class A:
#     @classmethod
#     def func(cls):
#         cls.静态属性名
#         cls.静态方法
#         cls.类方法


# class A:
#     @staticmethod
#     def func():
#         pass
