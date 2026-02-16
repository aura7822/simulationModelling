import numpy as np
import matplotlib.pyplot as plt

# Data
server_load = np.array([10, 20, 30, 40, 50, 60, 70, 80])
response_time = np.array([120, 135, 160, 180, 210, 250, 295, 350])

# Linear regression
coefficients = np.polyfit(server_load, response_time, 1)  # degree 1 for linear
slope = coefficients[0]
intercept = coefficients[1]
print(f"Regression line: y = {intercept:.2f} + {slope:.3f}x")

# Prediction for 90% server load
load_90 = 90
predicted_response = intercept + slope * load_90
print(f"Predicted response time at 90% load: {predicted_response:.2f} ms")

# Scatter plot
plt.scatter(server_load, response_time, color='blue', label='Data points')

# Regression line
x_line = np.linspace(0, 100, 200)
y_line = intercept + slope * x_line
plt.plot(x_line, y_line, color='red', label='Regression line')

# Labels and title
plt.xlabel('Server Load (%)')
plt.ylabel('Response Time (ms)')
plt.title('Server Load vs Response Time')
plt.legend()
plt.grid(True)

# Show plot
plt.show()