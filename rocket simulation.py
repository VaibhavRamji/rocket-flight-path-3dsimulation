import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
df = pd.read_csv('rocket_data.csv')  # Replace with your actual file name

# Extract data
time = df['Time (s)'].values
velocity = df['Velocity (m/s)'].values

# Estimate pitch angle (degrees): from 90 (vertical) to ~0 (horizontal)
pitch_deg = np.linspace(90, 5, len(time))  # Approximate gravity turn
pitch_rad = np.radians(pitch_deg)

# Decompose velocity
v_vertical = velocity * np.sin(pitch_rad)
v_horizontal = velocity * np.cos(pitch_rad)

# Integrate to get altitude and horizontal distance
altitude = np.cumsum(v_vertical * np.gradient(time))
horizontal_distance = np.cumsum(v_horizontal * np.gradient(time))

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(horizontal_distance, velocity, altitude, color='#1f77b4')
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Velocity (m/s)')
ax.set_zlabel('Altitude (m)')
plt.show()(m)')
plt.show()
