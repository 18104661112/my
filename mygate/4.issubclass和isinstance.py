# 两个内置函数说起

# issubclass(Son,Foo)
# 判断Son是否是Foo的子类
# 判断类与类之间是否有继承关系关系
# class Foo(object):pass
# class Son(Foo):pass
# ret = issubclass(Son,Foo)
# print(ret)

# isinstance(obj,cls)   #判断对象与类之间的关系,这个类也包括父类
# type()
# a = 1
# ret1 = type(a) is int
# ret2 = isinstance(a,int)
# print(ret1)
# print(ret2)

# class User(object):pass
# class VIPUser(User):pass
#
# alex = VIPUser()
# ret1 = type(alex) is User
# ret2 = isinstance(alex,User)
# print(ret1,ret2)
# ret1 = type(alex) is VIPUser
# ret2 = isinstance(alex,VIPUser)
# print(ret1,ret2)

# isinstance(obj,类)
    # 承认继承关系的
# 类 = type(obj)
    # 只承认实例化这个对象的那个类(不承认所有的继承关系)









