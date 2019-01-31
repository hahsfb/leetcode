#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 21. Merge Two Sorted Lists.py
@Author  : HaoQiangJian
@Site    : 
@Time    : 19-1-30 下午12:33
@Version : 
"""

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

"""
原文地址：　https://leetcode-cn.com/problems/valid-parentheses/
"""


# Definition for singly-linked list.
class Node(object):
    def __init__(self, val, p=None):
        self.val = val
        self.next = p


class ListNode:
    def __init__(self):
        self.head = 0

    def init_list(self, data):
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        return self

    def getlength(self):

        p = self.head
        length = 0
        while p:
            length += 1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() == 0:
            return True
        else:
            return False

    def insert(self, index, item):

        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty.')
            return

        if index == 0:
            q = Node(item, self.head)

            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            q = Node(item, p)
            post.next = q
            q.next = p

    def append(self, item):

        q = Node(item)
        if not self.head:
            self.head = q
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = q

    def getitem(self, index):
        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.val
        else:
            print('target is not exist!')


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode()
        l1_len = l1.getlength()
        l2_len = l2.getlength()
        for i in range(max(l1_len, l2_len)):
            l1_item = l1.getitem(i) if i < l1_len else None
            l2_item = l2.getitem(i) if i < l2_len else None

            if l1_item and l2_item and l1_item < l2_item:
                l.append(l1_item)
                l.append(l2_item)
            elif l1_item and l2_item and l1_item >= l2_item:
                l.append(l2_item)
                l.append(l1_item)
            elif l1_item and not l2_item:
                l.append(l1_item)
            elif l2_item and not l1_item:
                l.append(l2_item)
            else:
                pass
        return l


if __name__ == '__main__':
    l1 = ListNode().init_list([1, 2, 3, ])
    l2 = ListNode().init_list([1, 4, 5, ])

    print(l1.getlength())
    print(l1.getitem(3))
    print(l2.getlength())
    print(l1.getitem(1))

    result = Solution().mergeTwoLists(l1, l2)
    print(result)
