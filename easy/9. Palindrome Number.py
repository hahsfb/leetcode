#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 9. Palindrome Number.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 19-1-26 下午1:18
@Version : 
"""

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""

"""
原文地址： https://leetcode-cn.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        copy_x = x
        tem_int = 0
        while copy_x > 0:
            a = copy_x % 10
            copy_x //= 10
            tem_int = tem_int * 10 + a

        if tem_int == x:
            return True
        else:
            return False


if __name__ == '__main__':
    result = Solution().isPalindrome(122)
    print(result)

