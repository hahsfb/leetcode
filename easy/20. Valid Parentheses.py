#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 20. Valid Parentheses.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 19-1-26 下午3:18
@Version : 
"""

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

"""
原文地址：　https://leetcode-cn.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool  ['(', ')', '[', ']', '{', '}']
        """
        basic_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        s_l = len(s.strip())

        if s_l % 2 != 0:
            return False
        for i in s:
            if i not in basic_dict.keys():
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == basic_dict[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        # return True


if __name__ == '__main__':
    result = Solution().isValid("(()[]{})((")
    print(result)
