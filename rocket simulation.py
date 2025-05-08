import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Time settings
dt = 1
totaltime = 175

# Parameters
initial_mass = 13250    # kg
final_mass = 5427     # kg
cd = 0.22
crossectionalarea = 0.22 # m²
burn_rate = 70           # kg/s
initial_velocity = 0
thrust = 169006.41       # N
gravity = 9.81           # m/s²
initial_height = 0       # m
pitchover_alt = 40000    # m

# Initialization
mass = initial_mass
velocity = initial_velocity
height = initial_height
horizontal_distance = 0
pitch_angle = 90
pitchover_started = False

# Lists for plotting
mass_list = []
velocity_list = []
height_list = []
horizontal_list = []

# Simulation loop
for t in range(1,175):

    if height >= pitchover_alt and not pitchover_started:
        pitchover_started = True
        print("Pitchover started at", height, "meters")

    if pitchover_started:
        pitch_angle = 0.0000005
        pitch_angle = max(pitch_angle, 50)

    mass = initial_mass-burn_rate* dt*t
    a = (thrust - (mass * gravity)) / mass

    new_velocity = velocity + a * dt
    velocity = new_velocity

    vertical_velocity = velocity * np.sin(np.radians(pitch_angle))
    horizontal_velocity = velocity * np.cos(np.radians(pitch_angle))

    height += vertical_velocity * dt
    horizontal_distance += horizontal_velocity * dt

    # Store data
    mass_list.append(mass)
    velocity_list.append(velocity)
    height_list.append(height)
    horizontal_list.append(horizontal_distance)

    if mass <= final_mass:
        thrust = 0

# Plotting 3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(horizontal_list, velocity_list, height_list, color='purple')

ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Velocity (m/s)')
ax.set_zlabel ('Altitude (m)')
plt.show()
