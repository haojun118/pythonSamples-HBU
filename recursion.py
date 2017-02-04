# -*- coding: utf-8 -*-
# Date: 2017-02-04
# Authon: xshg
# 递归函数，求n的阶乘，调用函数求 10! 

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

print("10! = %d" % fact(10))
