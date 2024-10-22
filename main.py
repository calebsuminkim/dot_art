from turtle import Turtle, Screen
from make_image import Image

START_X = -500
START_Y = 480

drawer = Turtle()
screen = Screen()
image = Image()

# Setting up the screen
screen.screensize(700, 1000)
screen.colormode(255)

# Setting up the drawer
drawer.speed(0)


def draw_dot(b, g, r):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pencolor(b, g, r)  # RGB로 변환
    drawer.pendown()
    drawer.dot(5)


image_width, image_height = image.get_width_height()
#print(len(image.red)) # 570
#print(image_width) # 505
#print(image_height) # 570

x = START_X
y = START_Y
for i in range(0, image_height, 5):  # blue의 길이던, green의 길이던 red던 상관X
    for j in range(0, image_width, 5):
        blue_v = image.img[i, j, 0]
        green_v = image.img[i, j, 1]
        red_v = image.img[i, j, 2]
        draw_dot(blue_v, green_v, red_v)
        x += 5
        print(f"x : {x}, y : {y}")
        if x > 0 and x == image_width:
            y -= 5
            x = START_X



screen.exitonclick()
