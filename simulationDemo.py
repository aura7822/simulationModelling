import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


lambda_rate = 4  # arrival rate (students per hour)
mu_rate = 6      # service rate (students per hour)
n_customers = 20 # number of students to simulate


np.random.seed(42)


inter_arrival_times = np.random.exponential(scale=1/lambda_rate, size=n_customers)


service_times = np.random.exponential(scale=1/mu_rate, size=n_customers)


arrival_times = np.cumsum(inter_arrival_times)

# Initialize arrays
service_start = np.zeros(n_customers)
service_end = np.zeros(n_customers)
waiting_time = np.zeros(n_customers)
time_in_system = np.zeros(n_customers)


service_start[0] = arrival_times[0]
service_end[0] = service_start[0] + service_times[0]
waiting_time[0] = 0
time_in_system[0] = service_times[0]

# Process remaining customers
for i in range(1, n_customers):
    
    service_start[i] = max(arrival_times[i], service_end[i-1])
    service_end[i] = service_start[i] + service_times[i]
    waiting_time[i] = service_start[i] - arrival_times[i]
    time_in_system[i] = service_end[i] - arrival_times[i]


df = pd.DataFrame({
    'Student #': range(1, n_customers + 1),
    'Inter-arrival (hrs)': [f'{x:.4f}' for x in inter_arrival_times],
    'Arrival Time (hrs)': [f'{x:.4f}' for x in arrival_times],
    'Service Time (hrs)': [f'{x:.4f}' for x in service_times],
    'Service Start (hrs)': [f'{x:.4f}' for x in service_start],
    'Service End (hrs)': [f'{x:.4f}' for x in service_end],
    'Wait Time (hrs)': [f'{x:.4f}' for x in waiting_time],
    'Time in System (hrs)': [f'{x:.4f}' for x in time_in_system]
})

# Display the table
print("=" * 120)
print("M/M/1 QUEUE SIMULATION RESULTS (20 STUDENTS)")
print("=" * 120)
print(df.to_string(index=False))
print("=" * 120)

# Calculate simulated averages
sim_avg_wait = np.mean(waiting_time)
sim_avg_time_sys = np.mean(time_in_system)

# Theoretical values (from M/M/1 formulas)
theoretical_wait = lambda_rate / (mu_rate * (mu_rate - lambda_rate))  # Wq
theoretical_time_sys = 1 / (mu_rate - lambda_rate)  # Ws

print("\n SIMULATION SUMMARY")
print("-" * 50)
print(f"Simulated Average Waiting Time: {sim_avg_wait:.4f} hours ({sim_avg_wait*60:.2f} minutes)")
print(f"Simulated Average Time in System: {sim_avg_time_sys:.4f} hours ({sim_avg_time_sys*60:.2f} minutes)")
print(f"\n THEORETICAL VALUES (M/M/1)")
print("-" * 50)
print(f"Theoretical Average Waiting Time (Wq): {theoretical_wait:.4f} hours ({theoretical_wait*60:.2f} minutes)")
print(f"Theoretical Average Time in System (Ws): {theoretical_time_sys:.4f} hours ({theoretical_time_sys*60:.2f} minutes)")

# Calculate differences
wait_diff = abs(sim_avg_wait - theoretical_wait) * 60
sys_diff = abs(sim_avg_time_sys - theoretical_time_sys) * 60

print(f"\n COMPARISON")
print("-" * 50)
print(f"Waiting Time Difference: {wait_diff:.2f} minutes")
print(f"System Time Difference: {sys_diff:.2f} minutes")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Arrival and Service Times
axes[0,0].plot(range(1, n_customers+1), arrival_times, 'bo-', label='Arrival Times', markersize=4)
axes[0,0].plot(range(1, n_customers+1), service_end, 'rs-', label='Completion Times', markersize=4)
axes[0,0].set_xlabel('Student Number')
axes[0,0].set_ylabel('Time (hours)')
axes[0,0].set_title('Arrival and Completion Times')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# Plot 2: Waiting Times
axes[0,1].bar(range(1, n_customers+1), waiting_time*60, color='skyblue', edgecolor='navy')
axes[0,1].axhline(y=theoretical_wait*60, color='red', linestyle='--', label=f'Theoretical: {theoretical_wait*60:.2f} min')
axes[0,1].set_xlabel('Student Number')
axes[0,1].set_ylabel('Waiting Time (minutes)')
axes[0,1].set_title('Waiting Time per Student')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# Plot 3: Time in System
axes[1,0].bar(range(1, n_customers+1), time_in_system*60, color='lightgreen', edgecolor='darkgreen')
axes[1,0].axhline(y=theoretical_time_sys*60, color='red', linestyle='--', label=f'Theoretical: {theoretical_time_sys*60:.2f} min')
axes[1,0].set_xlabel('Student Number')
axes[1,0].set_ylabel('Time in System (minutes)')
axes[1,0].set_title('Time in System per Student')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

# Plot 4: Queue Length Over Time
time_points = np.sort(np.concatenate([arrival_times, service_end]))
queue_length = np.zeros(len(time_points))
for i, t in enumerate(time_points):

    queue_length[i] = np.sum((arrival_times <= t) & (service_end > t))

axes[1,1].step(time_points, queue_length, where='post', linewidth=2)
axes[1,1].fill_between(time_points, queue_length, step='post', alpha=0.3)
axes[1,1].set_xlabel('Time (hours)')
axes[1,1].set_ylabel('Queue Length')
axes[1,1].set_title('Queue Length Over Time')
axes[1,1].grid(True, alpha=0.3)
axes[1,1].set_ylim(bottom=0)

plt.tight_layout()
plt.show()

# Detailed analysis
print("\nDETAILED ANALYSIS:")
print("-" * 50)
print(f"Number of students who waited: {np.sum(waiting_time > 0)} out of {n_customers}")
print(f"Maximum waiting time: {np.max(waiting_time)*60:.2f} minutes")
print(f"Minimum waiting time: {np.min(waiting_time)*60:.2f} minutes")
print(f"Standard deviation of waiting time: {np.std(waiting_time)*60:.2f} minutes")