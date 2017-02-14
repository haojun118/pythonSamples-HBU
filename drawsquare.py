# -*- coding: utf-8 -*-

# Date: 2017-2-14
# Ver: 1.0
# Author: xshg
# 使用turtle库，绘制一个矩形

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")

    brad.forward(100)
    brad.right(90)
    
    brad.forward(100)
    brad.right(90)
    
    brad.forward(100)
    brad.right(90)
    
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()
