import cv2 as cv
from turtle import Turtle, Screen
from make_image import make_image
IMG_SRC = ["bae_live_400x400.png", "john.png", "john_2.png"]

drawer = Turtle()
screen = Screen()

# Setting up the screen
screen.screensize(400, 400)
screen.colormode(255)

# Setting up the drawer

drawer.speed(0)

print(screen.screensize())
print(screen.window_width())
print(screen.window_height())
blue, green, red = make_image(IMG_SRC[2])


def draw_dot(color_index):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pencolor(red[color_index], green[color_index], blue[color_index])
    drawer.pendown()
    drawer.dot(10)


x = -200
y = 200
for i in range(0, len(blue), 10):
    if i % 400 == 0:
        y -= 10
        x = -200
    x += 10
    draw_dot(i)


screen.exitonclick()
