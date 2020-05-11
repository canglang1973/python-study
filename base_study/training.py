#!usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: leitao
@time: 2020/5/8 0008 16:26
@desc:
"""
from array import array
from typing import List
import datetime
import asyncio

# file = open("C://Users/Administrator/Desktop/111.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# print(content.count('1'))

# def fun(a, b=None, c=None):
#     print(a, b, c)
#
#
# def fun2(*a, b=None, c=None):
#     print(*a, b, c)
#     print(a[0], a[2])
#     print(len(a))
#
#
# fun(1, 2, 3)
# fun(1, **{'b': 2, 'c': 3})
# fun2(1, 2, 3, 4, 5, 6, 7, **{'b': 2})
# print("1" not in "123")

"""

start = datetime.datetime.now()
fir = None
sec = None
with open("C://Users/Administrator/Desktop/1111.txt", "r", encoding="utf-8") as f:
    fir = {l.split("\t")[1].replace('\n', '') for l in f.readlines()}
with open("C://Users/Administrator/Desktop/111.txt", "r", encoding="utf-8") as f:
    sec = {l.replace('\n', '') for l in f.readlines()}
result = sec & fir
with open("C://Users/Administrator/Desktop/w.txt", "w", encoding="utf-8") as w:
    for l in result:
        w.writelines(l + '\n')
end = datetime.datetime.now()
print(start, end)
print("处理完成", (end - start).seconds)
"""

"""
class User(object):

    def __init__(self, name, age=None):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.getter
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.getter
    def age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def __str__(self):
        return self._name + ":" + str(self._age)
user = User("小明")
print(user)
print(user.age)
user.set_age(30)
print(user)
print(isinstance(user, set))
user.__setattr__("age", 20)
print(user)
print(user.__getattribute__("name"))
"""
"""
l = [1, 2, 3]
a = array('i', l)
print(a)
a.fromlist([4])
print(a)
a.reverse()
print(a)
"""

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
