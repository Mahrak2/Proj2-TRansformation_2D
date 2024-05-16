#!/usr/bin/env python3 
from  twod import Point2D
import numpy as np


class Transformation:
    def __init__(self, translate, rotate):
        self.translation = translate
        self.rotation = rotate
        self.delta_x = translate.translation_matrix[0, 2]
        self.delta_y = translate.translation_matrix[1, 2]
        self.theta = rotate.theta

        self.homogeneous_matrix = np.array([
            [np.cos(self.theta), -np.sin(self.theta), self.delta_x],
            [np.sin(self.theta), np.cos(self.theta), self.delta_y],
            [0, 0, 1]
        ])

    def __mul__(self, point):
        if isinstance(point, Point2D):
            transformed_coordinates = np.dot(self.homogeneous_matrix, point.coordinates)
            return Point2D(transformed_coordinates[0], transformed_coordinates[1])
        else:
            raise ValueError("Multiplication with wrong type.")
