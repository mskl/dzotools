# AUTOGENERATED! DO NOT EDIT! File to edit: 04_bilateral.ipynb (unless otherwise specified).

__all__ = ['point_gauss', 'bilateral_filter']

# Cell
import numpy as np

# Cell
def point_gauss(x: np.array, sigma: float) -> np.array:
    """Vectorised function to get pdf value for each element in x."""
    return np.exp(-(x - 0.0)**2 / (2 * sigma**2)) / (2*np.pi*np.sqrt(sigma))

# Cell
from tqdm import tqdm, trange
from .convolution import gauss2D


def bilateral_filter(
    arr: np.array,
    g_sigma: float,
    b_sigma: float,
    distance: str = "subtract",
    pad: str ="edge",
) -> np.array:
    """Apply a bilaterlar filter on the input (B/W) image data.

    Current implementation does not utilize any speedups
    and thus does not scale well when the (especially)
    g kernel is large. The kernel is generated in bounds
    of plus/minus 3 sigma.
    """

    # Select the distance function
    if distance == "subtract":
        dist_fun = np.subtract
    elif distance == "logsubtract":
        dist_fun = lambda x, y: np.log1p(x) - np.log1p(y)

    # The 2D gaussian filter precalculated for (-3, 3) sigma
    filter_g = gauss2D(g_sigma)

    # halfwidth not including the center <hw, c, hw>
    hw = filter_g.shape[0] // 2

    padded = np.pad(arr, pad_width=(hw, hw), mode=pad)
    result = np.zeros_like(padded, dtype="float32")

    for x in tqdm(range(hw, arr.shape[0] + hw)):
        for y in range(hw, arr.shape[1] + hw):
            center = padded[x, y]
            window = padded[x-hw: x+hw+1, y-hw: y+hw+1]

            # Compute the b filter and combine it with b filter
            # Utilize given distance function (e.g. log(x)-log(y))
            center_distance = dist_fun(center, window)
            filter_b = point_gauss(center_distance, b_sigma)
            filter_composite = filter_g * filter_b

            # Normalize the composite filter to preserve brightness
            normalization = 1 / np.sum(filter_composite)
            result[x, y] = normalization * np.sum(window * filter_composite)

    return result[hw:arr.shape[0] + hw, hw:arr.shape[1] + hw]