# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(234, 220, 200), (214, 159, 97), (208, 230, 215), (45, 107, 146), (125, 165, 192), (237, 212, 222), (202, 137, 159), (208, 220, 233), (125, 181, 155), (147, 65, 92), (39, 130, 95), (182, 161, 35), (159, 82, 51), (226, 201, 119), (197, 84, 110), (213, 88, 66), (60, 165, 133), (139, 28, 46), (234, 163, 180), (47, 160, 183), (159, 210, 191), (10, 104, 81), (112, 116, 167), (237, 169, 158), (22, 52, 80), (135, 33, 23), (33, 58, 113), (74, 34, 22), (150, 208, 218), (18, 63, 47)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(10, random.choice(color_list))
    tim.forward(30)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()