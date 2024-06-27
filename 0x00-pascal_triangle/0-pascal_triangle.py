#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    Args:
        n (int): The number of rows of the triangle.
    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    triangle = []
    if  n > 0:
        for i in range(1, n + 1):
            row = []
            row_value = 1
            for j in range(1, i + 1):
                row.append(row_value)
                row_value *= (i - j) // j
            triangle.append(row)
        return triangle
