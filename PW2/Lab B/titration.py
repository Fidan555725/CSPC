"""PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point."""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V, pH = data[:, 0], data[:, 1]

# TODO 2
slope = np.gradient(pH, V)
V_eq = V[np.argmax(slope)]
print("Equivalence point (mL):", V_eq)

# TODO 3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(V, pH)
ax1.axvline(V_eq, color="r", linestyle="--", label=f"{V_eq:.1f} mL")
ax1.set_xlabel("Volume of base (mL)")
ax1.set_ylabel("pH")
ax1.legend()

ax2.plot(V, slope)
ax2.axvline(V_eq, color="r", linestyle="--")
ax2.set_xlabel("Volume of base (mL)")
ax2.set_ylabel("dpH/dV")
fig.tight_layout()
fig.savefig("titration.png")