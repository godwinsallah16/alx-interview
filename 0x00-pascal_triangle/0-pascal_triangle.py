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
    if  n > 0:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
    else:
        return []

