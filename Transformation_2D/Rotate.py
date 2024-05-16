#!/usr/bin/env python3 

from  twod import Point2D
import numpy as np

class Rotate:
    def __init__(self, theta):
        self.rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        self.theta = theta

    def __add__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta + other.theta)
        else:
            raise ValueError("Addition with wrong type.")

    def __sub__(self, other):
        if isinstance(other, Rotate):
            return Rotate(self.theta - other.theta)
        else:
            raise ValueError("Subtraction with wrong type.")

    def __mul__(self, point):
        if isinstance(point, Point2D):
            rotated_coordinates = np.dot(self.rotation_matrix, point.coordinates)
            return Point2D(rotated_coordinates[0], rotated_coordinates[1])
        else:
            raise ValueError("Multiplication with wrong type.")

    def __repr__(self):
        return f"Rotate({self.theta})"
