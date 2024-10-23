from turtle import Turtle, Screen
from make_image import Image
import ceil_trunc

START_X = -340
START_Y = 490

drawer = Turtle()
screen = Screen()
image = Image()

# Setting up the screen
screen.screensize(800, 1000)
screen.colormode(255)

# Setting up the drawer
drawer.speed(0)


def draw_dot(x, y, color):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pencolor(color)  # 튜플 넘어옴
    drawer.pendown()
    drawer.dot(10)


image_width, image_height = image.get_width_height()
# print(len(image.red)) # 570
# print(image_width) # 485
# print(image_height) # 448

x = START_X
y = START_Y


def get_color(b, g, r):
    return r, g, b


for i in range(0, image_height, 10):
    for j in range(0, image_width, 10):
        blue_v = image.img[i, j, 0]
        green_v = image.img[i, j, 1]
        red_v = image.img[i, j, 2]
        draw_dot(x, y, get_color(blue_v, green_v, red_v))
        x += 10
        print(f"x : {x}, y : {y}")
        if x > 0 and x == ceil_trunc.ceil_trunc(image_width):
            y -= 10
            x = START_X

screen.exitonclick()
