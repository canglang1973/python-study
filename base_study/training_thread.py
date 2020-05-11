#!usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: leitao
@time: 2020/5/9 0009 16:54
@desc: 多线程
"""
import time
import _thread
import threading


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while 1:
    pass


