import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Time settings
dt = 0.1  # time step (s)
t_max = 150  # max simulation time (s)
t = np.arange(0, t_max, dt)

# Placeholder rocket parameters (adjust these based on your design)
initial_mass = 13350  # kg
dry_mass = 5427  # kg (after fuel is gone)
burn_rate = 72  # kg/s
thrust = 142006.41  # Increased thrust to improve ascent (adjust as needed)
drag_coefficient = 0.52  # Lower drag coefficient for better ascent
cross_section_area = 1.22  # m^2

# Constants
g = 9.81  # gravity (m/s^2)
air_density = 1.225  # kg/m^3 at sea level

# Initial conditions
vx, vy, vz = [0], [0], [300]  # Initial velocities (vertical boost for good ascent)
x, y, z = [0], [0], [0]
mass = initial_mass

# Check thrust-to-weight ratio
thrust_to_weight = thrust / (mass * g)
print(f"Initial Thrust-to-Weight Ratio: {thrust_to_weight:.2f}")

for i in range(1, len(t)):
    # Reduce mass due to fuel burn
    if mass > dry_mass:
        mass -= burn_rate * dt
    else:
        mass = dry_mass  # Ensure mass doesn't go below dry mass

    # Compute speeds
    speed = np.sqrt(vx[-1]**2 + vy[-1]**2 + vz[-1]**2)

    # Drag force (opposes velocity)
    drag = 0.5 * air_density * drag_coefficient * cross_section_area * speed**2

    # Simulate lateral thrust components (fx, fy)
    # Lateral thrust might be directed by guidance or wind, for now, we apply it randomly
    fx = 0.05 * thrust  # Example: 5% of thrust goes into the x direction
    fy = 0.05 * thrust  # Example: 5% of thrust goes into the y direction

    # Net thrust in the vertical direction
    fz = thrust - drag - mass * g  # Net thrust minus drag and gravity

    # Total acceleration
    ax = fx / mass
    ay = fy / mass
    az = fz / mass

    # Velocity update
    vx.append(vx[-1] + ax * dt)
    vy.append(vy[-1] + ay * dt)
    vz.append(vz[-1] + az * dt)

    # Position update
    x.append(x[-1] + vx[-1] * dt)
    y.append(y[-1] + vy[-1] * dt)
    z.append(z[-1] + vz[-1] * dt)

    # Stop if it hits the ground
    if z[-1] <= 0 and i > 10:
        break

# Plot 3D trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X (meters)')
ax.set_ylabel('Y (meters)')
ax.set_zlabel('Altitude (meters)')
plt.show()

# Output forces for debugging (just the last timestep here)
print("Final Forces (N):")
print(f"F_x = {fx}")
print(f"F_y = {fy}")
print(f"F_z = {fz}")
