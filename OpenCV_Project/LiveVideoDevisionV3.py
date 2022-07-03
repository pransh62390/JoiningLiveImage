import threading
import cv2
import numpy as np
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        time.sleep(1)
        t -= 1

webCam = cv2.VideoCapture(0)
webCam.set(3, 640)
webCam.set(4, 480)
webCam.set(10, 150)

temp = cv2.imread("img.jpg")
temp = cv2.resize(temp, (640, 480))
result = np.zeros_like(temp)
count = 0

def pec(countdown):
    print("start")
    countdown(10)
    global count

    if count == 0:
        result[0:240, 0:320] = img1
    elif count == 1:
        result[0:240, 320:640] = img2
    elif count == 2:
        result[240:480, 0:320] = img3
    elif count == 3:
        result[240:480, 320:640] = img4

    count += 1
    print("end")
    if count < 4:
        tmrthrd = threading.Thread(target=pec, args=(countdown,))
        tmrthrd.start()
    if count == 4:
        cv2.imwrite("./result.jpg", result)

tmrthrd = threading.Thread(target=pec, args=(countdown,))


while True:
    success, img = webCam.read()
    img1 = img[0:240, 0:320]
    img2 = img[0:240, 320:640]
    img3 = img[240:480, 0:320]
    img4 = img[240:480, 320:640]
    images = [img1, img2, img3, img4]

    for i in range(count, 4):
        if i == 0:
            result[0:240, 0:320] = img1
        elif i == 1:
            result[0:240, 320:640] = img2
        elif i == 2:
            result[240:480, 0:320] = img3
        elif i == 3:
            result[240:480, 320:640] = img4

    cv2.imshow("Image", result)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        tmrthrd.start()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
