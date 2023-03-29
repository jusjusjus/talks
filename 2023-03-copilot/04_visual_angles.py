"""Angles of visual perception

This file defines a function to compute how wide an object on a screen can be
displayed so that it falls within a given angle of visual perception.  Foveal,
parafoveal, and peripheral vision have approximate angles of 2, 10, and 60
degrees, respectively.
"""

import numpy as np

CHARACTER_WIDTH = 0.21  # cm
