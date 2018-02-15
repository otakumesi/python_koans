#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    if any([n < 1 for n in [a, b, c]]):
        raise TriangleError

    if is_triangle(a, b, c):
        return 'equilateral'
    elif is_isosceles(a, b, c):
        return 'isosceles'
    else:
        return 'scalene'


def is_triangle(a, b, c):
    ab = a == b
    ac = a == c
    return ab and ac


def is_isosceles(a, b, c):
    if a == b:
        if a > c:
            return True
        else:
            raise TriangleError
    if b == c:
        if b > a:
            return True
        else:
            raise TriangleError
    if a == c:
        if c > b:
            return True
        else:
            raise TriangleError
    return False


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
