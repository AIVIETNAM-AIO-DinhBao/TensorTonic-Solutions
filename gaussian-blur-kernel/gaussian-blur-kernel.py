import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    center = size//2
    kernel = []
    sum = 0.0
    for i in range(size):
        row = []
        for j in range(size):
            x,y = i - center, j - center
            val = math.exp(-(x**2 + y**2)/(2*sigma**2))
            row.append(val)
            sum += val
        kernel.append(row)
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= sum
    return kernel