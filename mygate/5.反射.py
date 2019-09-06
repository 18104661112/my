# 知识点
# 所有的a.b都可以变成getattr(a,'b')
# 用字符串数据类型的变量名 来获取实际的变量值
# 用字符串数据类型的变量名 找到这个变量对应的内存地址


# 使用对象反射
# obj.属性名
# obj.方法名()

# 使用类反射
# cls.静态变量名
# cls.类方法名()
# cls.静态方法名()

# 使用模块反射
# import time
# time.time()

# 调用函数和方法 地址+()
# def func():
#     print(1)

# func()
# a = func
# a()

# 反射当前文件


# 1.使用对象反射
# class Manager:   # 管理员用户
#     def __init__(self,name):
#         self.name  = name
#     def create_course(self):  # 创建课程
#         print('in Manager create_course')
#
#     def create_student(self): # 给学生创建账号
#         print('in Manager create_student')
#
#     def show_courses(self): # 查看所有课程
#         print('in Manager show_courses')
#
#     def show_students(self): # 查看所有学生
#         print('in Manager show_students')

# 不用反射
# alex = Manager('alex')
# operate_lst = ['创建课程','创建学生账号','查看所有课程','查看所有学生']
# for index,opt in enumerate(operate_lst,1):
#     print(index,opt)
# num = input('请输入您要做的操作 :')
# if num.isdigit():
#     num = int(num)
# if num == 1:
#     alex.create_course()
# elif num == 2:
#     alex.create_student()
# elif num == 3:
#     alex.show_courses()
# elif num == 4:
#     alex.show_students()

# 使用反射
# alex = Manager('alex')
# operate_lst = [('创建课程','create_course'),('创建学生账号','create_student'),
#                ('查看所有课程','show_courses'),('查看所有学生','show_students')]
# for index,opt in enumerate(operate_lst,1):
#     print(index,opt[0])
# num = input('请输入您要做的操作 :')
# if num.isdigit():
#     num = int(num)
#     if hasattr(alex,operate_lst[num-1][1]):
#         getattr(alex,operate_lst[num-1][1])()

# 如何使用反射
# alex = Manager('alex')
# print(alex.name)    # ==> print(getattr(alex,'name'))   用的相对少
# funcname = 'create_course'
# a = getattr(alex,funcname)
# b = alex.create_course
# print(a)
# print(b)
# getattr(alex,'create_course')()   # ==> # alex.create_course()   用的多

# 两种方式
    # 对象名.属性名 / 对象名.方法名() 可以直接使用对象的方法和属性
    # 当我们只有字符串数据类型的内容的时候
        # getattr(对象名,'方法名')()
        # getattr(对象名,'属性名')


# shop 买东西类
    # 1.浏览商品   scan_goods
    # 2.选择商品 ,添加到购物车  choose_goods
    # 3.删除商品   delete_goods

# class Shop:
#
#     def __init__(self,name):
#         self.name = name
#     def scan_goods(self):
#         print('%s正在浏览商品'%self.name)
#
#     def choose_goods(self):
#         print('%s正在选择商品'%self.name)
#
#     def delete_goods(self):
#         print('%s正在删除商品'%self.name)
#
# s = Shop('self哥')
# s.choose_goods()
# s.scan_goods()
# s.delete_goods()
# if hasattr(s,'choose_goods'):   # 判断s对象有没有choose_goods
#     func = getattr(s,'choose_goods')   # 使用s找到choose_goods对应的内存地址
#     print(func)
#     func()
# content = input('')
# if hasattr(s,content):   # 判断s对象有没有choose_goods
#     func = getattr(s,content)   # 使用s找到choose_goods对应的内存地址
#     print(func)
#     func()
# opt_lst = ['scan_goods','choose_goods','delete_goods']
# for index,opt in enumerate(opt_lst,1):
#     print(index,opt)
# num = int(input('num :'))
# if hasattr(s,opt_lst[num-1]):
#     getattr(s,opt_lst[num-1])()

# 和反射没关系
# for i in Shop.__dict__.keys():
#     if not i.startswith('__'):
#         print(i)


# 使用类反射
# class A:
#     Country = '中国'
#
#     @classmethod
#     def show(cls):
#         print('国家 : ',cls.Country)

# 'Country'
# print(getattr(A,'Country'))   # print(A.Country)
#
# A.show  # getattr(A,'show')
# 'show'
# getattr(A,'show')()   # A.show()

# 反射模块中的方法
import re
# ret = re.findall('\d+','2985urowhn0857023u9t4')
# print(ret)
# 'findall'
# getattr(re,'findall')   # re.findall
# ret = getattr(re,'findall')('\d','wuhfa0y80aujeiagu')
# print(ret)

# def func(a,b):
#     return a+b

# wahaha = func
# ret = wahaha(1,2)
# print(ret)

import time
# time.time  == getattr(time,'time')
# time.time()  == getattr(time,'time')()

# 'time'
# now  = getattr(time,'time')()
# print(now)

# time.sleep(1)
# print(321)
# getattr(time,'sleep')(1)   # time.sleep(1)
# print(123)

# 只要是a.b这种结构,都可以使用反射
# 用对象\类\模块反射,都只有以下场景
# 这种结构有两种场景
    # a.b   b是属性或者变量值
        # getattr(a,'b')   == a.b
    # a.b()  b是函数或者方法
        # a.b()
            # getattr(a,'b')()
        # a.b(arg1,arg2)
            # getattr(a,'b')(arg1,arg2)
        # a.b(*args,**kwargs)
            # getattr(a,'b')(*args,**kwargs)


# 反射本文件中的内容 :只要是出现在全局变量中的名字都可以通过getattr(modules[__name__],字符串数据类型的名字)
from sys import modules
# print(modules)    # DICT KEY是模块的名字,value就是这个模块对应的文件地址

# import re
# print(re)   # <module 're' from 'D:\\python3\\lib\\re.py'>
# print(modules['re'])
# 选课系统
# 're': <module 're' from 'D:\\python3\\lib\\re.py'>
# print(re.findall)
# print(modules['re'].findall)

# a = 1
# b = 2
# while True:
#     name = input('变量名 :')
#     print(__name__)
#     print(getattr(modules[__name__],name))

# '__main__': <module '__main__' from 'D:/PyCharmProject/s20/day23/5.反射.py'>
# print(a,b)
# print(modules['__main__'].a)
# print(modules['__main__'].b)
#
# print(getattr(modules['__main__'], 'a'))
# print(getattr(modules['__main__'], 'b'))


# 语法
# a = 1
# b = 2
# getattr(modules[__name__],'变量名')

# 函数名
# def func(a,b):
#     print('in func',a,b)
#
# getattr(modules[__name__],'func')   # func
# func(1,2)
# getattr(modules[__name__],'func')(1,2)   # func

# 类名
# class Course:
#     def func(self):
#         print('in func')
#
# print(Course)
# 'Course'
# print(getattr(modules[__name__],'Course'))   # Course
# getattr(modules[__name__],'Course')()   # 实例化的过程

'''
# 只要是a.b这种结构,都可以使用反射
# 用对象\类\模块反射,都只有以下场景
# 这种结构有两种场景
#     a.b   b是属性或者变量值
#         getattr(a,'b')   == a.b
#     a.b()  b是函数或者方法
#         a.b()
#             getattr(a,'b')()
#         a.b(arg1,arg2)
#             getattr(a,'b')(arg1,arg2)
#         a.b(*args,**kwargs)
#             getattr(a,'b')(*args,**kwargs)
# 如果是本文件中的内容,不符合a.b这种结构
    # 直接调用func()
        # getattr(sys.modules[__name__],'func')()
    # 直接使用类名 Person()
        # getattr(sys.modules[__name__],'Person')()
    # 直接使用变量名 print(a)
        # getattr(sys.modules[__name__],'a')
# 所有的getattr都应该和hasattr一起使用
    # if hasattr():
         getattr()
'''

class A:
    def qqxing(self):
        print('qqxing')

alex = A()
alex.name = 'sb'
# print(alex.name)

'name'
# setattr 能够通过字符串数据类型的变量名 给一个对象创建一个新的属性
# setattr(alex,'name','sb')   # alex.name = 'sb'
# print(alex.name)

# def wahaha(self):
#     print('wahaha',self.name)
#
# setattr(alex,'wahaha',wahaha)
# print(alex.__dict__)
# alex.wahaha(alex)

# delattr()
# print(alex.__dict__)
# delattr(alex,'name')   # del alex.name
# print(alex.__dict__)

'''
# hasattr和getattr
    # 只要是a.b这种结构,都可以使用反射
    # 用对象\类\模块反射,都只有以下场景
    # 这种结构有两种场景
    #     a.b   b是属性或者变量值
    #         getattr(a,'b')   == a.b
    #     a.b()  b是函数或者方法
    #         a.b()
    #             getattr(a,'b')()
    #         a.b(arg1,arg2)
    #             getattr(a,'b')(arg1,arg2)
    #         a.b(*args,**kwargs)
    #             getattr(a,'b')(*args,**kwargs)
    # 如果是本文件中的内容,不符合a.b这种结构
        # 直接调用func()
            # getattr(sys.modules[__name__],'func')()
        # 直接使用类名 Person()
            # getattr(sys.modules[__name__],'Person')()
        # 直接使用变量名 print(a)
            # getattr(sys.modules[__name__],'a')
    # 所有的getattr都应该和hasattr一起使用
        # if hasattr():
             getattr()
# setattr 只用来修改或者添加属性\变量,不能用来处理函数或者是其他方法
    # a.b = value
    # setattr(a,'b',value)
    
# delattr 只用来删除 属性\变量
    # del a.b 删除属性  相当于删除了a对象当中的b属性
    # delattr(a,'b')
'''