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
