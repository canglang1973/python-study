#!usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: leitao
@time: 2020-5-11 16:38
@desc:
"""
import pandas as pd
import numpy as np

# s = pd.Series([1, 2, 3], index=["a", "b", "b"])
# print(s)
# print(s.values)
# print(s.index)
# print(s['b'])

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print(df.head())
print(df["C"])
print(np.arange(6.))











