import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Parameters (replace placeholders with real values) ---
mass = 5000  # kg
thrust = 1.2e5  # N
burn_time = 30  # seconds
drag_coefficient = 0.5
cross_section_area = 1.0  # m²
air_density = 1.225  # kg/m³
time_step = 0.1
total_time = 520

# --- Arrays ---
times = np.arange(0, total_time, time_step)
x, y, z = [0], [0], [0]
vx, vy, vz = [0], [0], [0]

# --- Simulation loop ---
for t in times[1:]:
    speed = np.sqrt(vx[-1]**2 + vy[-1]**2 + vz[-1]**2)
    speed_capped = min(speed, 3000)

    # Drag
    drag = 0.5 * air_density * drag_coefficient * cross_section_area * speed_capped**2
    drag_x = drag * (vx[-1] / speed) if speed else 0
    drag_y = drag * (vy[-1] / speed) if speed else 0
    drag_z = drag * (vz[-1] / speed) if speed else 0

    # Pitch and yaw angles to spread thrust in X and Y
    if t <= burn_time:
        pitch = min(np.radians(30), np.radians(t))  # pitch angle
        yaw = min(np.radians(20), np.radians(t / 2))  # yaw angle

        fx = thrust * np.sin(pitch) * np.cos(yaw)
        fy = thrust * np.sin(pitch) * np.sin(yaw)
        fz = thrust * np.cos(pitch)
    else:
        fx = fy = fz = 0

    # Accelerations
    ax = (fx - drag_x) / mass
    ay = (fy - drag_y) / mass
    az = (fz - drag_z - mass * 9.81) / mass

    # Velocities
    vx.append(vx[-1] + ax * time_step)
    vy.append(vy[-1] + ay * time_step)
    vz.append(vz[-1] + az * time_step)

    # Positions
    x.append(x[-1] + vx[-1] * time_step)
    y.append(y[-1] + vy[-1] * time_step)
    z.append(z[-1] + vz[-1] * time_step)

# --- Plot 3D Path ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='3D Flight Path')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Altitude (m)')
ax.set_title("3D Rocket Trajectory with Pitch and Yaw")
ax.legend()
plt.show()
