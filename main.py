import cv2 as cv
import pyautogui as ag
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageChops


screenWidth, screenHeight = ag.size()

def highlighter(pil_image):
    pil_image.convert('RGBA')

    # Split into 4 channels
    r, g, b, a = pil_image.split()
    shadows = 1.8
    alpha = 1
    midtones = .8
    highlights = 1.2

    shadow_r = r.point(lambda i: i * shadows if(i < 85) else 0)
    shadow_g = g.point(lambda i: i * shadows if(i < 85) else 0)
    shadow_b = b.point(lambda i: i * shadows if(i < 85) else 0)
    shadow_a = a.point(lambda i: i * alpha if(i < 85) else 0)

    mid_r = r.point(lambda i: i * midtones if(i >= 85 and i < 170) else 0)
    mid_g = g.point(lambda i: i * midtones if(i >= 85 and i < 170) else 0)
    mid_b = b.point(lambda i: i * midtones if(i >= 85 and i < 170) else 0)
    mid_a = a.point(lambda i: i * alpha if(i >= 85 and i < 170) else 0)

    highlight_r = r.point(lambda i: i * highlights if(i >= 170) else 0)
    highlight_g = g.point(lambda i: i * highlights if(i >= 170) else 0)
    highlight_b = b.point(lambda i: i * highlights if(i >= 170) else 0)
    highlight_a = a.point(lambda i: i * alpha if(i >= 170) else 0)

    # Recombine back to RGB image
    shadow_img = Image.merge('RGBA', (shadow_r, shadow_g, shadow_b, shadow_a))
    mid_img = Image.merge('RGBA', (mid_r, mid_g, mid_b, mid_a))
    highlight_img = Image.merge('RGBA', (highlight_r, highlight_g, highlight_b, highlight_a))

    pil_image2 = ImageChops.add(shadow_img,mid_img)
    pil_image = ImageChops.add(pil_image2,highlight_img)
    return pil_image

def checkStatus():
    # pilScreen = ag.screenshot()
    pilScreen = Image.open("shakescreen.png")
    # cvScreen = cv.cvtColor(np.array(pilScreen),cv.COLOR_BGR2RGB)
    # cvShake = cv.imread("shake3.png")
    # cvFish = cv.imread("fish2.png")
    # cvScreen_b = cv.convertScaleAbs(cvScreen, alpha=.5, beta=1)
    # cvShake_b = cv.convertScaleAbs(cvShake, alpha=1, beta=120)
    # cvScreenGR = cv.cvtColor(cvScreen,cv.COLOR_RGB2GRAY)
    # cvFishGR =  cv.cvtColor(cvShake, cv.COLOR_RGB2GRAY)

    cvReel = cv.cvtColor(
        cv.convertScaleAbs(np.array(
            highlighter(pilScreen)), alpha=.5, beta=1),
        cv.COLOR_BGR2RGB)
    cvReelGR = cv.cvtColor(cvReel, cv.COLOR_RGB2GRAY)
    cvShake = cv.convertScaleAbs(np.array(pilScreen), alpha=1, beta=150)
    cvShakeGR = cv.cvtColor(cvShake,cv.COLOR_RGB2GRAY)

    cvFish = cv.cvtColor(
        cv.convertScaleAbs(np.array(
            highlighter(Image.open("fish2.png"))), alpha=.5, beta=1),
        cv.COLOR_BGR2RGB)
    cvFishGR =  cv.cvtColor(cvFish, cv.COLOR_RGB2GRAY)
    cvButton = cv.convertScaleAbs(cv.imread("shake3.png"), alpha=1, beta=150)
    cvButtonGR =  cv.cvtColor(cvButton, cv.COLOR_RGB2GRAY)

    # gamma = 2
    # gamma2=4
    # adjusted_image = np.power(cvScreenGR / 255.0, gamma) * 255.0
    # adjusted_image = adjusted_image.astype(np.uint8)
    # adjusted_image2 = np.power(cvScreenGR / 255.0, gamma2) * 255.0
    # adjusted_image2 = adjusted_image2.astype(np.uint8)
    # plt.figure(figsize=(10, 5))  # Create a figure with a specified size
    # plt.subplot(1, 3, 2)  # Subplot for the original image
    # plt.imshow(cv.cvtColor(adjusted_image, cv.COLOR_BGR2RGB))
    # plt.title("adjusted_image gamma =2")

    # plt.subplot(1, 3, 1)  # Subplot for the original image
    # plt.imshow(cv.cvtColor(cvScreenGR, cv.COLOR_BGR2RGB))
    # plt.title("Original Image")

    # plt.subplot(1, 3, 3)  # Subplot for the original image
    # plt.imshow(cv.cvtColor(adjusted_image2, cv.COLOR_BGR2RGB))
    # plt.title("Original Image gamma = 4")
    # plt.axis('off')
    # plt.show()


    # reeling = cv.imread("reelingscreen.png")
    # shake = cv.imread("shakescreen.png")

    # cv.imshow("reel", cv.convertScaleAbs(reeling, alpha=1.5, beta=1))
    # cv.imshow("shake", cv.convertScaleAbs(shake, alpha=1.5, beta=1))
    # cv.waitKey()
    alg = cv.SIFT_create()
    kp1, des1 = alg.detectAndCompute(cvShakeGR,None)
    kp2, des2 = alg.detectAndCompute(cvButtonGR, None)
    kp3, des3 = alg.detectAndCompute(cvReelGR,None)
    kp4, des4 = alg.detectAndCompute(cvFishGR, None)
    
    # screenKp = cv.drawKeypoints(temp, kp1, None)
    # shakeKp = cv.drawKeypoints(cvShakeGR, kp2, None)

    bf = cv.BFMatcher()

    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < .75*n.distance:
            good.append([m])
    print(f"{len(good)} - Shaking")
    cv.imshow("Shaking", cv.drawMatchesKnn(cvShakeGR,kp1,cvButtonGR,kp2,good,None,flags=2))

    matches = bf.knnMatch(des3, des4, k=2)
    good = []
    for m, n in matches:
        if m.distance < .5*n.distance:
            good.append([m])
    print(f"{len(good)} - Reeling")
    cv.imshow("Reeling", cv.drawMatchesKnn(cvReelGR,kp3,cvFishGR,kp4,good,None,flags=2))
    cv.waitKey()



checkStatus()

