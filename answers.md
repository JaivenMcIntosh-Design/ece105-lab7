# Lab 7: answers

Your name: Jaiven McIntosh

For each issue, fill in Reproduce to Confirm **before** you change any code. Then fix it and test it.

## Issue 3: report.py crashes

- Reproduce (the command, and the last line it printed): python report.py/ last line: 
AttributeError: 'Particle' object has no attribute 'gbest'. Did you mean: 'pbest'?
- Where (the lowest frame: file, line, and the code on that line): pso_v3.py, line 46 inside get_pbest , return self.gbest
- Hypothesis (one sentence):
- Confirm (an experiment of 1 to 3 lines, and what it printed):article.get_pbest() in pso_v3.py mistakenly Peferences self.gbest instead of self.pbest, raising an AttributeError because individual Particle instances only store their personal best (self.pbest) rather than a global best (gbest).
- Fix (the line before, and after; which file?):

In `pso_v3.py` (line 46), changed `return self.gbest` to `return self.pbest`.
- Test (its name; it failed before the fix, and passes after):

`test_get_pbest` in `test_pso_v3.py` (failed with `AttributeError` before the fix; passes after).

## Issue 4: the sphere crashes on [0, 10]

- Reproduce (the command, and the last line it printed):

python pso_v3.py sphere 2 20 0 10 100 / last line: ZeroDivisionError: division by zero

- Where (the lowest frame: file, line, and the code on that line):

pso_v3.py line 126
- Hypothesis (one sentence): why is the number you divide by exactly 0?

Because xmin = 0 sits right on sphere's minimum at (0, 0), particles that fly past 0 get clamped to exact 0.0 by np.clip, making the best fitness old = 0.0 20 iterations later and causing ZeroDivisionError


- Confirm (an experiment of 1 to 3 lines, and what it printed):

Ran pso_solve('sphere', s, 100, patience=1000) and printed best pbest: [0. 0.] first zero iter: 2

- What should the early stop do when the best value is exactly 0, and stays 0?
- Fix (the line before, and after):

n pso_v3.py (line 126), changed if (old - history[-1]) / old < tol: to if old == 0 or (old - history[-1]) / old < tol

- Test (its name; it failed before the fix, and passes after):

test_sphere_zero_bound_early_stop in test_pso_v3.py

## Issue 5: Rastrigin's answer is wrong

Reproduce: 
python pso_v3.py rastrigin 2 20 -5.12 5.12 100 / actual output: rastrigin: best x = [0. 1.6587], f(x) = 10, iterations run: 45 (expected $f(x) = 0$ at [0, 0]).   Where: pso_v3.py, inside rastrigin: return 10 * n + sum(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i]) for i in range(n - 1))

Hypothesis: 
rastrigin loops over range(n - 1) instead of range(n), completely omitting the last coordinate x[-1] from the sum while still adding 10 * n, which leaves a constant offset of +10 and ignores x[1] during optimization.Confirm: Ran python -c "from pso_v3 import rastrigin; print('origin [0, 0]:', rastrigin([0.0, 0.0]), 'point [0, 1]:', rastrigin([0.0, 1.0]))" and it printed origin [0, 0]: 10.0 point [0, 1]: 10.0 instead of 0.0 and 1.0.   

Fix: 
In pso_v3.py inside rastrigin, changed range(n - 1) to range(n).

Test: test_rastrigin_known_value_and_symmetry in test_pso_v3.py (failed with 10.0 == 0.0 before the fix; passes after).

## Three questions

1. Issue 3's bug was in `pso_v3.py` from the start, yet every run and all five of Wednesday's tests
   passed. Why?

   Neither pso_v3.py nor Wednesday's five unit tests ever called p.get_pbest(), accessing best.pbest directly instead, so the method went untested until report.py called it.

2. Issue 4: how can the best value be exactly 0.0? Why does the same run on [-10, 10] never crash?

Because xmin = 0 sits on sphere's minimum at (0, 0), particles that fly past 0 get clamped to exact 0.0 by np.clip, and 0.0**2 + 0.0**2 evaluates to exact 0.0.

3. Issue 5: the user guessed a local minimum. What showed that the swarm was not stuck?

Calling rastrigin([0.0, 0.0]) directly returned 10.0 instead of 0.0, and rastrigin([0.0, 1.0]) also returned 10.0 instead of 1.0. That proved the swarm actually found the true minimum on x[0] = 0 and only reported 10 because rastrigin ignored x[1] (range(n - 1)), not because the swarm was trapped in a local minimum
