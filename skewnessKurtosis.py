import matplotlib.pyplot as plt
import seaborn as sns

# Data
speeds = [28, 30, 35, 37, 40, 42, 45, 52, 55, 60, 62, 90, 110]

# Histogram + density
sns.histplot(speeds, kde=True, bins=10, color='skyblue')
plt.title('Distribution of Download Speeds')
plt.xlabel('Download Speed (Mbps)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()