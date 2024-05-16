#!/usr/bin/env python3 
from  twod import Point2D
import numpy as np

class Translate:
    def __init__(self, delta_x, delta_y):
        self.translation_matrix = np.array([
            [1, 0, delta_x],
            [0, 1, delta_y],
            [0, 0, 1]
        ])

    def __add__(self, other):
        if isinstance(other, Translate):
            return Translate(self.translation_matrix[0, 2] + other.translation_matrix[0, 2],
                             self.translation_matrix[1, 2] + other.translation_matrix[1, 2])
        else:
            raise ValueError("Addition with wrong type.")

    def __sub__(self, other):
        if isinstance(other, Translate):
            return Translate(self.translation_matrix[0, 2] - other.translation_matrix[0, 2],
                             self.translation_matrix[1, 2] - other.translation_matrix[1, 2])
        else:
            raise ValueError("Subtraction with wrong type.")

    def __mul__(self, point):
        if isinstance(point, Point2D):
            translated_coordinates = np.dot(self.translation_matrix, point.coordinates)
            return Point2D(translated_coordinates[0], translated_coordinates[1])
        else:
            raise ValueError("Multiplication with wrong type.")

    def __repr__(self):
        return f"Translate({self.translation_matrix[0, 2]}, {self.translation_matrix[1, 2]})"
