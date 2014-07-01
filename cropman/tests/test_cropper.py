#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Face-aware Image Cropper Tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for `cropper` module.

    :copyright: (c) 2014 by Ming YANG.
    :license: WTFPL (Do What the Fuck You Want to Public License).

    Run:
        cd <path-to-cropman>
        python -m cropman.tests.test_cropper
"""

import unittest
import cv2
import numpy as np
import base64
import hashlib
from cropman.cropper import Cropper


class TestCropper(unittest.TestCase):

    def setUp(self):
        self.cropper = Cropper()
        self.input = cv2.imdecode(np.array(bytearray(base64.decodestring('''
            /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODw
            wQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoI
            ChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKC
            goKCgoKCgoKCj/wAARCACFAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAA
            AAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhBy
            JxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpT
            VFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqr
            KztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QA
            HwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQ
            J3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRom
            JygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiI
            mKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk
            5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD6ewaMUtGKBhRRijFABWXruu2Wix
            K13J+8f7kS/eb/AOt71pSMscbO5wqgsT6Ada8JtE1DxZ4y1C9lfbDG4RN3IHGQo+gx
            n/OcK1X2a0OjD0favXZHaTfFXSbHUEt9XtrmzhcjFxjegz3bgYHuM16DFKk0SSwukk
            TgMrodwYHoQR1FeR+LvAF7rOnqgnt0ZegBbn65/wAK0PhDeT2Wr634YmYm30+OGW3H
            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'''))), 1)

    def test_multisize(self):
        results = []
        for h in xrange(10, 100, 20):
            for w in xrange(10, 100, 20):
                results += list(self.cropper.crop(self.input, w, h).flatten())
        print len(results)
        self.assertEqual(
            hashlib.md5(np.asarray(results)).hexdigest(),
            '76b20e37ea8f49b801907d9a11bbacc4')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()