class Manager:   # 管理员用户
    opt_lst = ['创建课程','给学生创建账号','查看所有课程','查看所有学生','查看所有学生的选课情况','退出']
    def __init__(self,name):
        self.name  = name
    def create_course(self):  # 创建课程
        print('in Manager create_course')

    def create_student(self): # 给学生创建账号
        print('in Manager create_student')

    def show_courses(self): # 查看所有课程
        print('in Manager show_courses')

    def show_students(self): # 查看所有学生
        print('in Manager show_students')

    def show_students_courses(self): # 查看所有学生的选课情况
        print('in Manager show_students_courses')

    def quit(self):
        exit()

#

class Student:
    opt_lst = ['查看所有课程', '查看已选课程', '选择课程', '退出']
    def __init__(self,name):
        self.name  = name

    def show_courses(self):  # 查看所有课程
        print('in Student show_courses')

    def show_selected_course(self):  # 查看已选课程
        print('in Student show_selected_course')

    def choose_course(self):         # 选择课程
        print('in Student choose_course')

    def quit(self):
        exit()

# 1.输入用户名和密码
# 2.程序判断 用户名密码 是否正确   获知身份
# 3.如果是学生
    # 1,2,3,4学生能做的事情
    # 让用户选择
# 4.如果是管理员
    # 1,2,3,4,5,6管理员能做的事
    # 让管理员选择
import hashlib
def get_md5(usr,pwd):
    md5 = hashlib.md5(usr.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()

def login(usr,pwd):
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            username,password,ident = line.strip().split('|')
            if usr == username and get_md5(usr,pwd) == password:
                return {'result':True,'identify':ident,'username':usr}
        else: return {'result':False}

def auth():
    opt_lst1 = ['登录','退出']
    while True:
        for index,opt in enumerate(opt_lst1,1):
            print(index,opt)
        num = int(input('请输入你要做的操作 :'))
        if num == 1:
            usr = input('username :')
            pwd = input('password :')
            ret = login(usr,pwd)
            if ret['result']:
                print('登录成功')
                return ret
            else:
                print('登录失败')
        elif num == 2:
            exit()


ret = auth()
print(ret)
if ret['result']:
    if ret['identify'] == 'Manager':
        manager = Manager(ret['username'])
        while True:
            for index,opt in enumerate(Manager.opt_lst,1):
                print(index,opt)
            num = int(input('请选择您要操作的序号 :'))
            if num == 1:
                manager.create_course()
            elif num == 2:
                manager.create_student()
            elif num == 3:
                manager.show_courses()
            elif num == 4:
                manager.show_students()
            elif num == 5:
                manager.show_students_courses()
            elif num == 6:
                manager.quit()
    elif ret['identify'] == 'Student':
        student = Student(ret['username'])
        while True:
            for index,opt in enumerate(Student.opt_lst,1):
                print(index,opt)
            num = int(input('请选择您要操作的序号 :'))
            if num == 1:
                student.show_courses()
            elif num == 2:
                student.show_selected_course()
            elif num == 3:
                student.choose_course()
            elif num == 4:
                student.quit()



# 登录 一个用户在一台电脑上只能登录三次,三次之后就锁住了
# 在函数里不能用print
    # 模块 写一个函数完成一个功能

