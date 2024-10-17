import cv2 as cv


def make_image(image_src):
    print("make_image func is triggered from [make_image.py]")
    img = cv.imread(image_src)
    blue = []
    green = []
    red = []
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            blue.append(int(img[x, y][0]))
            green.append(int(img[x, y][1]))
            red.append(int(img[x, y][2]))

    return blue, green, red

#cv.imshow("Display window", img)
#k = cv.waitKey(1000) # Wait for a keystroke in the window
