import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    results = []
    dict = {}
    for word in vocab:
        dict[word] = 0
    for token in tokens:
        if token in dict:
            dict[token] += 1
    for word in dict:
        results.append(dict[word])
    return np.array(results)