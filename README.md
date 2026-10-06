# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A CSPC repository with Git version control, a conda environment, and a radioactive decay simulation (pure-Python loop and NumPy versions), tested with pytest.

**Speed comparison (loop vs NumPy):**
- loop : 2.6575 s
- numpy : 0.0003 s
- speed-up: 8846.5x faster

**Tests:** all passing? (yes)

**Conclusion:**
- The NumPy vectorised version is dramatically faster than the pure-Python loop because it processes all atoms at once instead of one at a time. I learned how to set up a reproducible Python environment with conda, use Git branching and remotes, and write pytest tests that check both error handling and statistical correctness within a tolerance.


---

## PW1 - Lab B: Data, Plotting, and Automation

**What I built:**
- A plot.py script that reads the observed decay data, computes the analytical decay curve, and produces a side-by-side comparison figure (figure.png).
- A Snakefile that automates the figure generation: it rebuilds figure.png only when decay_observed.csv or plot.py change, and does nothing when nothing changed.

**Result:**
- The observed data and the analytical curve (N0 * exp(-lambda * t)) match closely in shape on the shared axes, confirming the decay follows the expected exponential law.

**Conclusion:**
- Snakemake makes the pipeline reproducible: instead of rerunning python plot.py by hand every time, a single `snakemake --cores 1 figure.png` command checks file timestamps and only redoes work when inputs have actually changed.

## PW2 — Lab A

**Mean acceleration:** -8.58 m/s² (standard deviation = 28.72 m/s²). The mean is close to the expected -9.81 m/s², which confirms the object is in free fall.

**Why the acceleration is noisy:** A derivative compares nearby measurements, so it amplifies the measurement noise. The acceleration comes from differentiating twice, so the noise is amplified twice. This is why the acceleration values swing wildly (std much larger than the mean) while the position data looks smooth.

**Integrating back:** Integration is a sum, so random noise partly cancels out. Integrating the noisy acceleration twice recovered the position with a maximum difference of 0.78 m from the original, which shows that integration suppresses noise.

![motion](PW2/Lab%20A/motion.png)

**Bonus:** From `trajectory.csv` I plotted the x-y path and computed the speed with `np.gradient` on each coordinate (mean speed ≈ 23.65 m/s). Figure: `PW2/Lab A/trajectory.png`.

## PW2 — Lab B

**Part 2 (three methods):** On the convex function f(x) = (x-3)^2 + 1, gradient descent, Newton and SLSQP all reach x ≈ 3. On g(x) = x^4 - 3x^2 + x + 5 the methods do not always agree. From x0 = 0, Newton converged to x ≈ 0.17, where g'' < 0, so it is a maximum (a stationary point, not a minimum), while gradient descent and SLSQP found the minimum at x ≈ -1.30. From x0 = 2, gradient descent and Newton found the local minimum at x ≈ 1.13 (g'' > 0), while SLSQP found the global minimum at x ≈ -1.30. So the starting point and the algorithm both matter on a complicated landscape.

**Part 3 (rate constant):** The fitted first-order rate constant is k ≈ 0.262, close to the expected 0.25, and the fitted curve passes through the data.

**Part 4 (equilibrium):** Newton and SLSQP agree: x ≈ 0.664. Equilibrium composition: H2 = 0.336 mol, I2 = 0.336 mol, HI = 1.328 mol.

**Part 5 (titration, bonus):** The equivalence point is at 50 mL, where the slope of the pH curve is largest.