# -*- coding: utf-8 -*-
"""
    Cropman Library - Detector
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implements face detection functions.

    :copyright: (c) 2014 by Ming YANG.
    :license: WTFPL (Do What the Fuck You Want to Public License).
"""

import cv2
import os

# ----------------------------------------------------------------------------

DEFAULT_DATA_FILENAME = os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'config/haarcascade_frontalface_default.xml'
    )

class Detector(object):
    """Detector"""
    def __init__(self, data_filename = DEFAULT_DATA_FILENAME):
        super(Detector, self).__init__()
        self.face_cascade  = cv2.CascadeClassifier(data_filename)

    def detect_faces(self, img):
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray)
        return faces

# ----------------------------------------------------------------------------
