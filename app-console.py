#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Cropman Console
    ~~~~~~~~~~~~~~~

    Face-aware image cropper application (console interface).

    :copyright: (c) 2014 by Ming YANG.
    :license: WTFPL (Do What the Fuck You Want to Public License).

    Usage:
      app-console.py <input-image> <target-width> <target-height> <target-image>

    Options:
      -h --help     Show this screen.
      --version     Show version.
"""

from cropman.cropper import Cropper
from docopt import docopt
import cv2

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Cropman Console 0.1.0')
    input_filename = arguments['<input-image>']
    target_filename = arguments['<target-image>']
    target_width = int(arguments['<target-width>'])
    target_height = int(arguments['<target-height>'])

    cropper = Cropper()
    input_image = cv2.imread(input_filename)
    if input_image is None:
        print 'Invalid input image. Please check %s' % input_filename
    else:
        target_image = cropper.crop(input_image, target_width, target_height)
        if target_image is None:
            print 'Cropping failed.'
        else:
            cv2.imwrite(target_filename, target_image)
            print '\nDone. \nResult: %s' % target_filename

