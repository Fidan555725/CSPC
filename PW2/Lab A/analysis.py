"""
PW2 Lab A -- Motion from tracking data.
Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

# TODO 1
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", a.mean())

print("Std of acceleration:", a.std())

# TODO 3
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

diff = np.abs(y - y_recovered)
print("Max difference in recovered position:", diff.max())

# TODO 4
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

ax1.plot(t, y)
ax1.set_ylabel("Position (m)")

ax2.plot(t, v)
ax2.set_ylabel("Velocity (m/s)")

ax3.plot(t, a)
ax3.axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s²")
ax3.set_ylabel("Acceleration (m/s²)")
ax3.set_xlabel("Time (s)")
ax3.legend()

fig.savefig("motion.png")

# ---- BONUS: 2D trajectory ----
data2 = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t2, x2, y2 = data2[:, 0], data2[:, 1], data2[:, 2]

vx = np.gradient(x2, t2)
vy = np.gradient(y2, t2)
speed = np.sqrt(vx**2 + vy**2)
print("Mean speed:", speed.mean())

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x2, y2)
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_title("Path")
ax1.set_aspect("equal")

ax2.plot(t2, speed)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.set_title("Speed")

fig2.tight_layout()
fig2.savefig("trajectory.png")

**Bonus:** From `trajectory.csv` I plotted the x-y path and computed the speed with `np.gradient` on each coordinate (mean speed ≈ 23.65 m/s). Figure: `PW2/Lab A/trajectory.png`.