# -*- coding: utf-8 -*-
"""
    Cropman Library - Cropper
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Implements face-ware image cropping functions.

    :copyright: (c) 2014 by Ming YANG.
    :license: WTFPL (Do What the Fuck You Want to Public License).
"""

import sys
from detector import Detector

# ----------------------------------------------------------------------------

class Cropper(object):
    """Cropper"""
    def __init__(self):
        super(Cropper, self).__init__()
        self.detector  = Detector()

    @staticmethod
    def _bounding_rect(faces):
        top,    left  =  sys.maxint,  sys.maxint
        bottom, right = -sys.maxint, -sys.maxint
        for (x, y, w, h) in faces:
            if x < left:
                left = x
            if x+w > right:
                right = x+w
            if y < top:
                top = y
            if y+h > bottom:
                bottom = y+h
        return top, left, bottom, right

    def crop(self, img, target_width, target_height):
        original_height,  original_width  = img.shape[:2]
        faces = self.detector.detect_faces(img)
        if len(faces) == 0: # no detected faces
            target_center_x = original_width / 2
            target_center_y = original_height / 2
        else:
            top, left, bottom, right  = self._bounding_rect(faces)
            target_center_x = (left + right) / 2
            target_center_y = (top + bottom) / 2
        target_left = target_center_x - target_width / 2
        target_right = target_left + target_width
        target_top = target_center_y - target_height / 2
        target_bottom = target_top + target_height
        if target_top < 0:
            delta = abs(target_top)
            target_top += delta
            target_bottom += delta
            if target_bottom > original_height:
                target_bottom = original_height
        if target_left < 0:
            delta = abs(target_left)
            target_left += delta
            target_right += delta
            if target_right > original_width:
                target_right = original_width
        return img[target_top:target_bottom, target_left:target_right]

# ----------------------------------------------------------------------------
