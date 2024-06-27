#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    Args:
        n (int): The number of rows of the triangle.
    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("The number of rows must be a positive integer. Please retry with a positive number.")

        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
    except ValueError as e:
        print(e)
        return []
