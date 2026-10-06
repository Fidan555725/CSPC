"""PW2 Lab B Part 2 -- three routes to a minimum."""
import numpy as np
from scipy.optimize import newton, minimize


def gradient_descent(df, x0, lr=0.05, tol=1e-8, max_iter=100000):
    x = x0
    for _ in range(max_iter):
        step = lr * df(x)
        x = x - step
        if abs(step) < tol:
            break
    return x


# ---------- 2A: easy convex function ----------
def f(x):   return (x - 3)**2 + 1
def df(x):  return 2*(x - 3)
def d2f(x): return 2.0

x0 = 0.0
print("=== 2A: f(x) = (x-3)^2 + 1, x0 = 0 ===")
print("Gradient descent:", gradient_descent(df, x0))
print("Newton          :", newton(df, x0, fprime=d2f))
print("SLSQP           :", minimize(lambda x: f(x[0]), [x0], method="SLSQP").x[0])


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in (0.0, 2.0):
    print(f"\n=== 2B: g(x) = x^4 - 3x^2 + x + 5, x0 = {x0} ===")
    gd = gradient_descent(dg, x0, lr=0.01)
    print(f"Gradient descent: x = {gd:.6f}, g = {g(gd):.6f}")

    nw = newton(dg, x0, fprime=d2g)
    kind = "minimum" if d2g(nw) > 0 else "maximum"
    print(f"Newton          : x = {nw:.6f}, g = {g(nw):.6f}, g'' = {d2g(nw):.4f} -> {kind}")

    sl = minimize(lambda x: g(x[0]), [x0], method="SLSQP").x[0]
    print(f"SLSQP           : x = {sl:.6f}, g = {g(sl):.6f}")