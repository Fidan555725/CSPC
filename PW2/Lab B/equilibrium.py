"""PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1
def k_imbalance(x):
    return (2*x)**2 / ((a - x)*(b - x)) - K

# TODO 2: root-finding
x_newton = newton(k_imbalance, 0.5)

# TODO 3: minimisation
res = minimize(lambda x: k_imbalance(x[0])**2, [0.5], method="SLSQP",
               bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("Newton x:", x_newton)
print("SLSQP  x:", x_slsqp)
print("Agree:", np.isclose(x_newton, x_slsqp, atol=1e-4))

# TODO 4
x_eq = x_newton
print(f"H2 = {a - x_eq:.4f} mol, I2 = {b - x_eq:.4f} mol, HI = {2*x_eq:.4f} mol")

x = np.linspace(0, 0.999, 300)
plt.figure()
plt.plot(x, a - x, label="H2")
plt.plot(x, b - x, "--", label="I2")
plt.plot(x, 2*x, label="HI")
plt.axvline(x_eq, color="k", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("Extent x (mol)")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")
