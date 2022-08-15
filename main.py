# import colorgram
#
# rgb_colors = []
# hirst_colors = colorgram.extract("image.jpg", 30)
# for color in hirst_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

colors = [(237, 40, 115), (142, 27, 70), (219, 162, 59), (238, 71, 36), (14, 144, 89), (182, 166, 43), (31, 126, 191),
          (54, 190, 229), (245, 221, 50), (179, 41, 96), (128, 190, 101), (78, 27, 81), (39, 172, 118), (250, 225, 1),
          (210, 61, 31), (214, 131, 167), (150, 29, 26), (24, 194, 220), (239, 163, 194), (163, 212, 174),
          (244, 167, 150), (7, 110, 54), (137, 212, 230), (53, 136, 204), (83, 28, 27), (156, 197, 231)]
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setx(-225)
tim.sety(-225)
t.colormode(255)
for i in range(10):
    tim.setpos(-225, -225 + 50 * i)
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)

screen = t.Screen()
screen.exitonclick()
