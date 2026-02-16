import numpy as np
import matplotlib.pyplot as plt


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


numbers = lcg(seed=12345, n=10000)


plt.hist(numbers, bins=30, color='pink', edgecolor='black')
plt.title("LCG RNG Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


def runs_test(data):
    runs = 1
    for i in range(1, len(data)):
        if (data[i] > data[i - 1]) != (data[i - 1] > data[i - 2] if i > 1 else False):
            runs += 1
    return runs

print("Runs Test:", runs_test(numbers))