#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : Reverse_Integer.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 19-1-26 上午9:59
@Version : 
"""

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

"""
原文地址： https://leetcode-cn.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        ret_x = ''
        if x < 0:
            ret_x = '-'
            x = abs(x)

        str_x = str(x)
        if str_x[-1] == '0':
            str_x = str_x[:-1]

        for i in range(len(str_x)-1, -1, -1):
            ret_x += str_x[i]

        ret_x = int(ret_x)

        if -2**31 < ret_x < 2**31 - 1:
            return ret_x

        return 0


if __name__ == '__main__':
    result = Solution().reverse(120)
    print(result)
