# AUTOGENERATED! DO NOT EDIT! File to edit: 01_monadic.ipynb (unless otherwise specified).

__all__ = ['brightness', 'contrast', 'equalize']

# Cell
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

# Cell
def brightness(arr: np.array, adjust: int) -> np.array:
    """Adjust the brightness of the image."""
    # Apply the adjustment on each value of the ndarray
    return clipvals(arr + adjust)

# Cell
def contrast(arr: np.array, adjust: float) -> np.array:
    """Adjust the contrast of the image."""
    # Apply the adjustment on each value of the ndarray
    return clipvals(arr * adjust)

# Cell
def equalize(arr: np.array) -> np.array:
    """Change the input array by equalizing the histogram.
    This is applied on all pixels so be advised when called on RGB input.
    """

    # Count the values
    ctr = Counter(arr.flatten())
    # Sort the histogram dictionary
    histdict = dict(sorted(ctr.items(), key=lambda x: x[0]))
    # Create a second dict with cdf
    cumdict = dict(zip(histdict.keys(), np.cumsum(list(histdict.values()))))

    cmin = list(cumdict.values())[0]
    cmax = list(cumdict.values())[-1]

    # Normalize and count the values
    normvals = ((np.array([*cumdict.values()]) - cmin) / (cmax - cmin))
    normalised = np.round(normvals * 255).astype("int")

    # Apply the dictionary by vectorizing
    normdict = dict(zip(cumdict.keys(), normalised))
    return np.vectorize(normdict.get)(arr)