#!/usr/bin/env python3 

import numpy as np
from matplotlib import pyplot as plt

class Point2D:
    def __init__(self, x=0, y=0):
        self.coordinates = np.array([x, y, 1])

    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.coordinates[0] + other.coordinates[0],
                           self.coordinates[1] + other.coordinates[1])
        else:
            raise ValueError("Addition with wrong type.")

    def __sub__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.coordinates[0] - other.coordinates[0],
                           self.coordinates[1] - other.coordinates[1])
        else:
            raise ValueError("Subtraction with wrong type.")

    def __lt__(self, other):
        if isinstance(other, Point2D):
            return (self.coordinates[0], self.coordinates[1]) < (other.coordinates[0], other.coordinates[1])
        else:
            raise ValueError("Comparison with wrong type.")

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return np.array_equal(self.coordinates, other.coordinates)
        else:
            raise ValueError("Comparison with wrong type.")

    def __repr__(self):
        return f"Point2D({self.coordinates[0]}, {self.coordinates[1]})"

    def plot(self, color='b', marker='o', label=None):
        plt.plot(self.coordinates[0], self.coordinates[1], marker, color=color, label=label)
        plt.xlabel('X')
        plt.ylabel('Y')
