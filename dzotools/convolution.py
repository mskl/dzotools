# AUTOGENERATED! DO NOT EDIT! File to edit: 03_convolution.ipynb (unless otherwise specified).

__all__ = ['gauss1D', 'conv1D', 'separable_blur', 'gauss2D', 'conv2D']

# Cell
import numpy as np

# Cell
def gauss1D(sigma: float, bounds: tuple = (-3, 3)) -> np.array:
    """Get normalized kernel bounded by given sigma bounds."""
    domain = np.arange(bounds[0]*sigma, bounds[1]*sigma + 1)
    kernel = np.exp(-(domain - 0.0)**2 / (2 * sigma**2))
    return kernel / np.sum(kernel)

# Cell
def conv1D(row: np.array, cfilter: np.array, pad="edge") -> np.array:
    """
    Do a 1D convolution of a given filter over the input array.

    Edges are padded with pad strategy, input and output size match.
    Param `pad` controls padding. Eg. `constant` or `edge`.
    """

    # halfwidth not including the center <hw, c, hw>
    hw = len(cfilter) // 2

    # When hw is 2, we get padded array (0, 0, a, a, a, 0, 0)
    padded = np.pad(row, pad_width=(hw, hw), mode=pad)
    result = np.zeros_like(padded, dtype="float32")

    for c in range(hw, len(row) + hw):
        result[c] = np.dot(padded[c-hw: c+hw+1], cfilter)

    return result[hw:len(row)+hw]

# Cell
def separable_blur(arr: np.array, sigma: float, pad="edge") -> np.array:
    """
    Apply the gaussian blur by separable gaussian convolutions over 2D input.
    Note that this method currently only supports B/W (2 channel) inputs.
    """

    kernel = gauss1D(sigma)
    result = np.zeros_like(arr, dtype="float32")

    for x in range(arr.shape[0]): # columns
        result[:, x] = conv1D(arr[:, x], kernel, pad)
    for y in range(arr.shape[1]): # rows
        result[y, :] = conv1D(result[y, :], kernel, pad)

    return result

# Cell
def gauss2D(sigma: float, bounds: tuple = (-3, 3)) -> np.array:
    """Get normalized 2D gauss kernel bounded by sigma bounds."""
    domain = np.arange(bounds[0]*sigma, bounds[1]*sigma + 1)
    dom_x, dom_y = np.meshgrid(domain, domain)
    kernel = np.exp(-(dom_x**2 + dom_y**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

# Cell
def conv2D(arr: np.array, cfilter: np.array, pad="edge") -> np.array:
    """Do a 2D convolution of a given filter over the input array."""

    # Assume that the filter is symmetrical.
    assert cfilter.shape[0] == cfilter.shape[1]

    # halfwidth not including the center <hw, c, hw>
    hw = cfilter.shape[0] // 2

    # When hw is 2, we get padded array (0, 0, a, a, a, 0, 0)
    padded = np.pad(arr, pad_width=(hw, hw), mode=pad)
    result = np.zeros_like(padded, dtype="float32")

    for x in range(hw, arr.shape[0] + hw):
        for y in range(hw, arr.shape[1] + hw):
            # Sum the element-wise product of matrix multiplication
            result[x, y] = np.sum(padded[x-hw: x+hw+1, y-hw: y+hw+1] * cfilter)

    return result[hw:arr.shape[0] + hw, hw:arr.shape[1] + hw]