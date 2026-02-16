import numpy as np
import matplotlib.pyplot as plt

# LCG parameters
a = 1664525
c = 1013904223
m = 2**32

def lcg(seed, n=10000):
    x = seed
    nums = []
    for _ in range(n):
        x = (a * x + c) % m
        nums.append(x)
    return np.array(nums)

# Generate numbers
numbers = lcg(seed=12345, n=10000)
print("Generated:", len(numbers), "numbers")