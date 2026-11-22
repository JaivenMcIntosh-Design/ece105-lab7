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
- Where (the lowest frame: file, line, and the code on that line):
- Hypothesis (one sentence): why is the number you divide by exactly 0?
- Confirm (an experiment of 1 to 3 lines, and what it printed):

- What should the early stop do when the best value is exactly 0, and stays 0?
- Fix (the line before, and after):
- Test (its name; it failed before the fix, and passes after):


## Issue 5: Rastrigin's answer is wrong

- Reproduce (the command, and what it printed):
- Expected (what, and why):
- Hypothesis (one sentence): is the swarm stuck, or is something else wrong?
- Confirm (an experiment of 1 to 3 lines, and what it printed):
- Fix (the line before, and after):
- Test (its name; it failed before the fix, and passes after):

## Three questions

1. Issue 3's bug was in `pso_v3.py` from the start, yet every run and all five of Wednesday's tests
   passed. Why?
2. Issue 4: how can the best value be exactly 0.0? Why does the same run on [-10, 10] never crash?
3. Issue 5: the user guessed a local minimum. What showed that the swarm was not stuck?
