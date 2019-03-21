#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : list.py
@Author  : 
@Site    : 
@Time    : 19-3-11 下午2:37
@Version : 
"""
import numpy as np
from typing import overload, Optional

if __name__ == '__main__':
    # a = np.arange(24)
    # print (a.ndim)             # a 现只有一个维度
    # # 现在调整其大小
    # b = a.reshape(2,4,3)  # b 现在拥有三个维度
    # print (b.ndim)
    #
    # np.ones(1, dtype=None, order='C')
    a = np.arange(10)
    s = slice(2, 7, 2)  # 从索引 2 开始到索引 7 停止，间隔为2
    print(a[s])

b = np.array([1,2,3])
bb = np.tile(b, (4, 1))