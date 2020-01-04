#-*-coding:utf-8-*-
# Author:Lu Wei


#1.sys.path.append("/root/mods")的作用？
#导入python模块时，按照sys.path中的路径去挨个查找。

#2.字符串如何进行反转？
# v='asdfghjkqwertyui'
# v1=v[::-1]
# print(v1)

#3.不用中间变量交换a和b的值。
# a=1
# b=2
# a,b=b,a
# print(a,b)

#4.*args和**kwargs这俩参数是什么意思？我们为什么要用它。
#*args 位置参数转为元组，**kwargs关键字参数转为字典

#5.函数的参数传递是地址还是新值？
#函数参数传递为地址

#6.看代码写结果：
# my_dict = {'a':0,'b':1}
# def func(d):
#     d['a'] = 1
#     return d
#
# func(my_dict)
# my_dict['c'] = 2
# print(my_dict)
#my_dict = {'a':1,'b':1,'c':2}

#7.什么是lambda表达式
#匿名函数，简单表达式

#8.range和xrang有什么不同？
#py2 中，range直接生成，xrange执行的时候才会调用

#9."1,2,3" 如何变成 ['1','2','3',]
# a='1,2,3'
# print(a.split(','))

#10,['1','2','3'] 如何变成 [1,2,3]
# l1=['1','2','3']
# l2=[]
# for i in l1:
#     l2.append(int(i))
# print(l2)

#11.def f(a,b=[]) 这种写法有什么陷阱？
#b=[] 如果执行函数时没有传入自己的list，那就会使用b=[]，会造成没有传入自己list的执行时候，共用这个b=[] list。

#12.如何生成列表 [1,4,9,16,25,36,49,64,81,100] ，尽量用一行实现。
#
# v=[pow(i,2) for i in range(1,11)]
# print(v)

#13.python一行print出1~100偶数的列表, (列表推导式, filter均可)
# v=[i for i in range(1,101) if i%2==0]
# v1=filter(lambda x:x%2==0,range(1,101))
# print(list(v1))

#14.把下面函数改成lambda表达式形式
# def func():
#     result = []
#     for i in range(10):
#         if i % 3 == 0:
#             result.append(i)
#     return result

#15.如何用Python删除一个文件？
# import shutil
# shutil.rmtree()

#16.如何对一个文件进行重命名？
# import os
# os.rename('原文件名字','后文件名字')

#17.python如何生成随机数？
# import random
# v=random.randint(1,10)
# print(v)

#18.从0-99这100个数中随机取出10个数，要求不能重复，可以自己设计数据结构。
# import random
# a=set()
# while True:
#     v = random.randint(0, 100)
#     a.add(v)
#     if len(a)==10:
#         break
# print(a)

#19.用Python实现 9*9 乘法表 （两种方式）
# for i in range(1,10):
#     if i !=1:
#         print()
#     for j in range(1, i+1):
#         n=i*j
#         print('%s*%s=%s'%(i,j,n),end=' ')

#20.请给出下面代码片段的输出并阐述涉及的python相关机制。
# def dict_updater(k,v,dic={}):
#     dic[k] = v
#     print(dic)
# dict_updater('one',1)
# dict_updater('two',2)
# dict_updater('three',3,{})


#21.写一个装饰器出来。
# def func(arg):
#     def inner(*args,**kwargs):
#         return arg(*args,**kwargs)
#     return inner
# @func
# def index():
#     pass
#
# index()

#22.用装饰器给一个方法增加打印的功能。
# def func(arg):
#     def inner(*args,**kwargs):
#         print('asd')
#         return arg(*args,**kwargs)
#     return inner
# @func
# def index():
#     pass
#
# index()


#23.as 请写出log实现(主要功能时打印函数名)
'''
def log(arg):
    def inner(*args,**kwargs):
        print()
        return arg(*args,**kwargs)
    return inner

@log
def now():
    print("2013-12-25")

now()

# 输出
# call now()
# 2013-12-25


def dec_name(f):
    name = f.__name__
    def new_f(*a, **ka):
        return f(*a, __name__ = name, **ka)
    return new_f
@dec_name
def fun_name(x, __name__):
    print(__name__)
z = fun_name
z(1)'''


#24.
import requests,json # 需要先安装requests模块：pip install requests
d=[]
response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
data=json.loads(response.text)

# 获取结构中的所有name字段，使用逗号链接起来，并写入到 catelog.txt 文件中。
with open('catelog.txt',mode='w',encoding='utf-8') as f:
    for i in data['data']:
        d.append(i['name'])
    context=','.join(d)
    f.write(context)
"""
[
    {'id': 1, 'name': 'Python', 'hide': False, 'category': 1}, 
    {'id': 2, 'name': 'Linux运维', 'hide': False, 'category': 4}, 
    {'id': 4, 'name': 'Python进阶', 'hide': False, 'category': 1}, 
    {'id': 7, 'name': '开发工具', 'hide': False, 'category': 1}, 
    {'id': 9, 'name': 'Go语言', 'hide': False, 'category': 1},
    {'id': 10, 'name': '机器学习', 'hide': False, 'category': 3}, 
    {'id': 11, 'name': '技术生涯', 'hide': False, 'category': 1}
]
"""