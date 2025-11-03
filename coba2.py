import numpy as np
from scipy import stats

# Data acak
data = [10, 12, 9, 14, 13, 15, 9, 12]

# Hitung mean, median, mode menggunakan SciPy
print("Mean:", stats.tmean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True))
