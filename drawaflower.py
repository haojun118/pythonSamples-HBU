# -*- coding: utf-8 -*-

# Date: 2017-2-14
# Ver: 1.0
# Author: xshg
# 使用turtle库，绘制一朵花

import turtle

def draw_diamond(obj):
    obj.forward(100)
    obj.right(30)
    obj.forward(100)
    obj.right(150)
    obj.forward(100)
    obj.right(30)
    obj.forward(100)

def do_draw():
    
    window = turtle.Screen()
    flower = turtle.Turtle()
    flower.color("red")
    flower.speed(6)

    for i in range(36):
        draw_diamond(flower)
        flower.setheading((i+1) * 10)   # setheading(degree), degree 0 -> east, 90 -> north, 180 -> west, 270 -> south 

    flower.setheading(270)
    flower.forward(300)

    window.exitonclick()

do_draw()
