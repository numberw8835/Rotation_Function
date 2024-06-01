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

n = 3
period = 2
data = []

matrix = np.random.randint(0, 10, size=(n, n))
org_det = np.linalg.det(matrix)
data.append(org_det)
for i in range(period):
    rot_det = None
    while org_det != rot_det:
        matrix = Rot(matrix)
        rot_det = np.linalg.det(matrix)
        data.append(rot_det)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data with markers
ax.plot(data, marker='o', linestyle='-', color='royalblue', linewidth=2)

# Add text labels above each data point
for i, y in enumerate(data):
    ax.text(i, y, f"{y:.2f}", ha='center', va='bottom', fontsize=10)  # Adjust formatting as needed

# Customize labels, title, gridlines (same as before)
ax.set_xlabel("Rot$^{n}$(A)", fontsize=14)
ax.set_ylabel("Det(A)", fontsize=14)
ax.set_title(f'Determinant vs. Rotations of Matrix A_{n}x{n}, and Segment = {period}', fontsize=16)
ax.grid(axis='y', linestyle='--')
ax.tick_params(axis='both', which='major', labelsize=12)

# Show the plot
plt.tight_layout()
plt.show()