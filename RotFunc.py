import numpy as np
import matplotlib.pyplot as plt

def Rot(matrix):
    """Rotates elements within each ring of a matrix one position clockwise.

    Args:
        matrix: A list of lists representing the matrix.

    Returns:
        The matrix with elements rotated within their rings.
    """
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)

    if matrix.size == 0:  # Check if empty using size
        return matrix

    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top < bottom and left < right:
        prev = matrix[top + 1][left]  # Store the top-left corner value

        # Rotate top row
        for i in range(left, right):
            matrix[top][i], prev = prev, matrix[top][i]

        # Rotate right column
        for i in range(top, bottom):
            matrix[i][right], prev = prev, matrix[i][right]

        # Rotate bottom row
        for i in range(right, left, -1):
            matrix[bottom][i], prev = prev, matrix[bottom][i]

        # Rotate left column
        for i in range(bottom, top, -1):
            matrix[i][left], prev = prev, matrix[i][left]

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return matrix


def determinant(matrix):
    """Calculates the determinant of a square matrix.

    Args:
        matrix: A list of lists or a NumPy array representing the square matrix.

    Returns:
        The determinant of the matrix.

    Raises:
        ValueError: If the input matrix is not square.
    """
    if not isinstance(matrix, np.ndarray):  # Convert if not a NumPy array
        matrix = np.array(matrix)

    if matrix.size == 0:
        return 1

    if len(matrix) != len(matrix[0]):
        raise ValueError("Input must be a square matrix.")

    n = len(matrix)

    if n == 1:
        return matrix[0][0]  # Base case: 1x1 matrix

    det = 0
    for j in range(n):
        cofactor = matrix[0][j] * determinant(get_cofactor(matrix, 0, j))
        det += (-1) ** j * cofactor
    return det


def get_cofactor(matrix, row, col):
    return [[matrix[i][j] for j in range(len(matrix[0])) if j != col]
            for i in range(len(matrix)) if i != row]
