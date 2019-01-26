#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 14. Longest Common Prefix.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 19-1-26 下午2:05
@Version : 
"""

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

"""
原文地址：　https://leetcode-cn.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        len_list = [len(i) for i in strs]
        min_len = min(len_list)
        min_index = len_list.index(min_len)

        min_str = strs[min_index]
        if not min_str:
            return ''
        tmp_str = ''
        for i in range(1, len(min_str) + 1):
            tmp_str = min_str[:i]
            for s in strs:
                if tmp_str != s[:i]:
                    if i > 0:
                        return min_str[:i-1]
        return tmp_str


if __name__ == '__main__':
    result = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(result)
