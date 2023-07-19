# import colorgram
#
# # extract colors
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
#
# rgb_colors = []
# # create a for loop that taps into each of the colors
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module

turtle_module.colormode(255)
spice = turtle_module.Turtle()
spice.speed("fastest")
spice.penup()
spice.hideturtle()

color_list = [(241, 237, 228), (236, 238, 244), (245, 237, 242), (235, 243, 239), (185, 162, 132), (129, 92, 70),
              (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92),
              (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98),
              (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118),
              (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

spice.setheading(225)
spice.forward(300)
spice.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    spice.dot(20, random.choice(color_list))
    # repeat process
    spice.forward(50)

    if dot_count % 10 == 0:
        # create painting
        spice.setheading(90)
        spice.forward(50)
        spice.setheading(180)
        spice.forward(500)
        spice.setheading(0)


# create a new screen object
screen = turtle_module.Screen()
screen.exitonclick()