def average_pooling_2d(X: list, pool_size: int) -> list:
    """
    Returns non-overlapping average-pooled windows.
    """
    # Write code here
    height = len(X)
    width = len(X[0])
    out_height = height // pool_size
    out_width = width // pool_size
    output = []

    for i in range(out_height):
        row = []
        for j in range(out_width):
            start_row = i * pool_size
            start_col = j * pool_size
            total = 0.0
            for a in range(pool_size):
                for b in range(pool_size):
                    total += X[start_row + a][start_col + b]
            average = total/(pool_size**2)
            row.append(average)
        output.append(row)
    return output