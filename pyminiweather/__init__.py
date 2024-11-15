import os
from enum import IntEnum

if int(os.environ.get("PYMW_USE_NUMPY", 0)) != 0:
    import numpy as numpy
    from scipy.signal import convolve as convolve
else:
    import cunumeric as numpy
    from cunumeric import convolve as convolve

print(f"Imported numpy backend: {numpy.__name__}")


class IDS(IntEnum):
    DENS = 0
    UMOM = 1
    WMOM = 2
    RHOT = 3
