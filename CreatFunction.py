#python定义函数使用def语句
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x
#
# print(my_abs(100))

#参数个数的错误可以自动检查
# my_abs(1,2)
#参数类型的错误不能自动检查，需要自己写检查语句

#前面函数的完善
# def mybas(x):
#     if not isinstance(x,(float,int)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# mybas('aaa')

#定义空函数用pass语句
#pass的作用：用来作为占位符
# if 0>=18:
#     pass

#返回多个值
import math
def move(x,y,step,angle=0):
    nx = x+step * math.cos(angle)
    ny = y-step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)
#这样虽然是返回了两个值，但其实这是一种假象，Python函数返回的仍然是单一值
r=move(100,100,60,math.pi/6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。