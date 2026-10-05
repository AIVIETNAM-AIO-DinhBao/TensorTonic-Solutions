def image_histogram(image: list) -> list:
    """
    Returns a list of intensity and count pairs.
    """
    # Write code here
    count = {}
    for row in image:
        for pixel in row:
            if pixel in count:
                count[pixel] += 1
            else: count[pixel] = 1
    results = []
    for i in sorted(count.keys()):
        results.append([i, count[i]])
    return results