from unittest import result

import cv2
import unittest

global i
i=0
def QrDetecting(img):
    # обнаружить и декодировать
    data, bbox, _ = detector.detectAndDecode(img)
    # проверяем, есть ли на изображении QRCode
    if bbox is not None:
        if data:
            print("[+] QR Code detected, data:", data)
            i =1
    else:
        print("[-] QR Code is not detected")
        i = 2
    return(i)

    # отобразить результат
    cv2.imshow("img", img)
detector = cv2.QRCodeDetector()
if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    # инициализируем детектор QRCode cv2
    while True:
        _, img = cap.read()
        QrDetecting(img)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
