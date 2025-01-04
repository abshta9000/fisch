import cv2 as cv
import pyautogui as ag
import numpy as np
from matplotlib import pyplot as plt

screenWidth, screenHeight = ag.size()

def shaking():
    pilScreen = ag.screenshot()
    cvScreen = cv.cvtColor(np.array(pilScreen),cv.COLOR_BGR2RGB)
    cvShake = cv.imread("shake3.png")
    # cvScreen = cv.imread("shakescreen.png")
    cvScreenBGR = cv.cvtColor(cvScreen,cv.COLOR_RGB2BGR)
    cvScreenGR = cv.cvtColor(cvScreen,cv.COLOR_RGB2GRAY)
    cvShakeGR =  cv.cvtColor(cvShake, cv.COLOR_RGB2GRAY)
    w, h = cvShake.shape[:-1]
    W, H = cvScreen.shape[:-1]
    print(str(W) + " "+ str(H))
    # cv.imshow("Original Image", cvScreen)
    
    # cv.waitKey()


    ret, thresh = cv.threshold(cvShakeGR, 240, 255, cv.THRESH_BINARY)

    cvShakeGR[thresh == 255] = 0

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    erosion = cv.erode(cvShakeGR, kernel, iterations = 1)

    cvScreen_b = cv.convertScaleAbs(cvScreen, alpha=1, beta=170)
    cvShake_b = cv.imread("shake4.png")
    # cv.imshow("Original Image", cvShake_b)
    # cv.moveWindow("Original Image", 1000,800)
    # cv.waitKey()
    # cv.imshow("Original Image", cv.imread("shake4.png"))
    # cv.waitKey()
    # cvScreen_bc = cv.convertScaleAbs(cvScreen_b, alpha=1.2, beta=0)
    # cv.imshow("Original Image", cvScreen_bc)
    # cv.waitKey()
    # cvScreen_bce = cv.convertScaleAbs(cvScreen_bc, alpha=1.2, beta=0)
    # cv.imshow("Original Image", cvScreen_bce)
    # cv.waitKey()



    # res = cv.matchTemplate(cv.cvtColor(cvScreen_b,cv.COLOR_RGB2GRAY), cvShakeGR, cv.TM_SQDIFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # top_left = min_loc
    # bottom_right = (top_left[0] + w, top_left[1] + h)
    # cv.rectangle(cvScreen, top_left, bottom_right, (0, 0, 255), 2)
    i=0
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
            # blue          green       red            white        black           gray
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255), (128, 128, 128)]
    for meth in methods:
        img = cv.cvtColor(cvScreen_b, cv.COLOR_RGB2GRAY).copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img,cv.cvtColor(cvShake_b,cv.COLOR_RGB2GRAY),method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        if top_left[1] >= len(res) or top_left[0] >= len(res[0]):
            print("Unsuccessful - " + meth)
            continue
        print(str(res[top_left[1]][top_left[0]]))
        # print(str(top_left) + " " + meth)
        # print(str(res))
        # loc = np.where( res >= .8)
        # for pt in zip(*loc[::-1]):
        #     cv.rectangle(cvScreen, pt, (pt[0] + w, pt[1] + h), colors[methods.index(meth)], 2)
        #     print(i)
        #     i+=1
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv.rectangle(img,top_left, bottom_right, colors[methods.index(meth)], 2)
        # plt.subplot(121),plt.imshow(res)
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(img)
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.suptitle(meth)
        # plt.show()
        cv.rectangle(cvScreen, top_left, bottom_right, colors[methods.index(meth)], 2)
    show = cv.resize(cvScreen, (1500,1000))
    cv.imshow("Original Image", show)
    cv.waitKey()

shaking()

