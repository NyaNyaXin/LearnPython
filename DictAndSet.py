# dict(dictionary)
# #定义一个dict和获取一个dict中的key所对应的value
# d = {'ChenXin':99,'DingJianHui':20}
# print(d['ChenXin'])
# #给key赋值
# d['Admin']=67
# print(d['Admin'])
#
# #使用in判断key是否存在于一份dict中
# a = 'Admin' in d
# print(a)
#
# #使用get方法判断是否存在
# print(d.get('aaa',-1))
#
# #删除key使用pop方法
# d.pop('ChenXin')
# print(d)

#set
#要创建一个set需要提供一个list作为输入集合
#set和dict类似，也是一组key的集合，但不存储value。
#由于key不能重复，所以，在set中，没有重复的key。
# s = set([1,1,2,3,2,3])
# print(s)
# #使用add方法向set中添加元素
# s.add(4)
# print(s)
# #使用remove方法删除set中的元素
# s.remove(1)
# print(s)
#set的交集与并集操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)
print(s2|s1)