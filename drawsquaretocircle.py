# -*- coding: utf-8 -*-

# Date: 2017-2-14
# Ver: 1.0
# Author: xshg
# 使用turtle库，绘制一个个矩形，形成一个圆形

import turtle

def draw_square(obj_turtle):
    for i in range(4):
        obj_turtle.forward(100)
        obj_turtle.right(90)

def do_draw():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    
    for i in range(36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

do_draw()
