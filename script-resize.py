#!/usr/bin/env python

import numpy as np

from skimage.transform import resize


resize_debug = np.load('resize-debug.npy')

resized = resize(resize_debug, [400,400], order=0)

np.save('resized', resized)

