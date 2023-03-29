"""Angles of visual perception

This files defines a function to compute how wide an object on
a screen can be displayed so that it falls within a given angle
of visual perception.  A character on screen is about 0.21 cm
wide.  Foveal, parafoveal, and peripheral vision have approximate
angles of 2, 10, and 60 degrees, respectively.
"""
import numpy as np

CHARACTER_WIDTH = 0.21  # cm
