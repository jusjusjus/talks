"""Angles of visual perception

This files defines a function to compute how wide an object on
a screen can be displayed so that it falls within a given angle
of visual perception.
"""
import numpy as np

CHARACTER_WIDTH = 0.21  # cm


def compute_width(angle: float, distance: float) -> float:
    """Compute width of object on screen

    Args:
        angle (float): Angle of visual perception in radians
        distance (float): Distance between observer and screen

    Returns:
        float: Width of object on screen in cm
    """
    return 2 * distance * np.tan(angle / 2) * 100


if __name__ == "__main__":
    # Compute width of object on screen
    for angle in (2.0, 10.0, 60.0):
        width = compute_width(angle=np.deg2rad(angle), distance=1)
        num_chars = width // CHARACTER_WIDTH
        print(f"Angle: {angle} deg, Width: {width:.2f} cm, Number of characters: {num_chars:.2f}")
