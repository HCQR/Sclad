import unittest
import cv2

import QrDetectingV2.py


img = cv2.imread("aboba.png")
img1 = cv2.imread("colombus.png")

class TestQRCase (unittest.TestCase):


   # img = cv2.imread("aboba.png")

    def test_QrEst(self):
       # global img
        self.assertEqual(QrDetected.QrDetecting(img),1)

    def test_QrNet(self):
       # global img
        self.assertEqual(QrDetected.QrDetecting(img1),2)

if __name__ == '__main__':
    unittest.main()

