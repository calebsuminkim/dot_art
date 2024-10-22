import cv2 as cv
IMG_SRC = ["bae_live_400x400.png", "john.png", "john_2.png", "mondrian.jpg"]


class Image:
    def __init__(self):
        self.img = cv.imread(IMG_SRC[-1])
        # self.blue = self.img[:, :, 0]   # img[x, y, 색상 정보(0:blue, 1:green, 2:red]
        # self.green = self.img[:, :, 1]
        # self.red = self.img[:, :, 2]

    def get_width_height(self):
        # TODO: 이미지 가로, 세로 구하기
        print("get_width_height func is triggered from [make_image.py]")
        img_width = self.img.shape[1]    # 열의 개수 == 세로
        img_height = self.img.shape[0]   # 행의 개수 == 가로
        return img_width, img_height

        # for x in range(img.shape[0]):
        #     for y in range(img.shape[1]):
        #         blue.append(int(img[x, y][0]))
        #         green.append(int(img[x, y][1]))
        #         red.append(int(img[x, y][2]))


    #cv.imshow("Display window", img)
    #k = cv.waitKey(1000) # Wait for a keystroke in the window
