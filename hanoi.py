# -*- coding: utf-8 -*-

# Date: 2017-02-11
# Ver: 1.0
# Author: xshg 
# 递归实现汉诺塔
# n 表示n层汉诺塔
# a柱为塔所在原始柱
# b为借助使用的柱
# c为塔最终所在柱

N = 3   #设初始塔高为3，可自由修改

def hanoi(n, a, b, c):
    if (n == 1):
        print("%c -> %c" % (a, c))
    else:
        hanoi(n-1, a, c, b)
        print("%c -> %c" % (a, c))
        hanoi(n-1, b, a, c)

hanoi(N , 'A', 'B', 'C')
