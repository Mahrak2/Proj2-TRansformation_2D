#!/usr/bin/env python3 
import sys
import os
import numpy as np
from matplotlib import pyplot as plt

# Get the absolute path to the Transformation_2D directory
Transformation_2D_dir = "/home/malhosani/Desktop/Intro_to_programming/Proj2/Transformation_2D"

# Add the 'Transformation_2D' directory to the Python path
sys.path.append(Transformation_2D_dir)

# Import Transformation_2D modules after adding the path
from twod import Point2D
from Rotate import Rotate
from Transformation import Transformation
from Translate import Translate


# Set up the points
points = [Point2D(2, 4), Point2D(3, 6), Point2D(), Point2D(1, 2)]
for p in points:
    print(p)

# Set up the transformations
t1 = Translate(1, 0)
r1 = Rotate(np.pi/8)
T1 = Transformation(t1, r1)
print(t1, r1, T1)

# Do operations with points
points.sort()
p_total = Point2D()
for p in points:
    p_total = p_total + p
    print(p)
print(p_total)

# Do operations with transformations
print(t1+t1)
print(r1+r1)
for p in points:
    p.plot('r')   #red
    p_t = t1 * p
    p_t.plot('b') #blue
    p_r = r1 * p
    p_r.plot('g') #green
    p_T = T1 * p
    p_T.plot('y') #yellow

plt.axis('equal')   
plt.show()
