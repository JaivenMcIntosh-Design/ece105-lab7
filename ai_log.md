# AI log: Lab 7

Your name:Jaiven Mcintosh

Tool: ChatGPT Edu (if you used another, say which)
Gemini Hydrogen 

For each issue: what you asked, what it said, and whether it was right. Paste both exactly; you may
cut parts of the answer that have nothing to do with the bug.

## Issue 3: report.py crashes

### My prompt

I run: python report.py
I get this traceback:

Traceback (most recent call last):
  File "report.py", line 18, in <module>
    print(f"{rank}. f= {p.get_fitness():.3g} at {np.round(p.get_pbest(), 4)}")
  File "pso_v3.py", line 46, in get_pbest
    return self.gbest
AttributeError: 'Particle' object has no attribute 'gbest'. Did you mean: 'pbest'?
I expected: It to print the top 5 particles' fitness values and personal best (pbest) positions.
The function in the lowest frame:

Python
def get_pbest(self):
    return self.gbest
What could make self.gbest fail here? Give me one or two hypotheses I can test. Don't change any code yet.

### Its answer (word for word)
Particle.get_pbest() in pso_v3.py mistakenly references self.gbest instead of self.pbest, raising an AttributeError because individual Particle instances only store their personal best (self.pbest) rather than a global best (gbest).
### Right, partly right, or wrong? How do you know?
confirmed buy running from pso_v4 particle: p..... it printed true, false, confirming Particle stores self.pbest and has no gbest attribute.
(Did it fix `pso_v3.py`, or change `report.py` so the error goes away?)

## Issue 4: the sphere crashes on [0, 10]

### My prompt
I run: python pso_v3.py sphere 2 20 0 10 100
I get a ZeroDivisionError: division by zero at line 126 in pso_solve on if (old - history[-1]) / old < tol:.
When run on [-10, 10], it finishes with f(x) = 2.3e-17 and no crash.
Why can old become exact 0.0 on [0, 10]? Give me one or two hypotheses I can test. Don't change any code yet.
### Its answer (word for word)
Because xmin = 0 sits right on the global minimum of sphere at (0, 0), when particles fly past 0 into negative territory, np.clip(..., 0, 10) clamps their coordinates to exact 0.0. That makes sphere([0.0, 0.0]) == 0.0, so old (the best fitness patience = 20 iterations later) becomes 0.0 and triggers ZeroDivisionError in (old - history[-1]) / old < tol.
### Right, partly right, or wrong? How do you know?
Right. Running pso_solve('sphere', s, 100, patience=1000) printed best pbest: [0. 0.] first zero iter: 2, confirming particles hit exact [0. 0.] via boundary clipping at iteration 2, making old equal to 0.0 twenty iterations later
(Did it say why the number was exactly 0, or only that you cannot divide by 0? With its fix, does the
run still stop early?)

## Issue 5: Rastrigin's answer is wrong

### My prompt
I run: python pso_v3.py rastrigin 2 20 -5.12 5.12 100
It outputs: rastrigin: best x = [0. 1.6587], f(x) = 10, iterations run: 45
Rastrigin's docstring says its minimum is 0 at the origin.
Here is the rastrigin function:

Python
def rastrigin(x):
    """Rastrigin's function, any dimension. Minimum 0 at the origin, and many local minima."""
    n = len(x)
    return 10 * n + sum(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i]) for i in range(n - 1))
Why does rastrigin([0.0, 1.6587]) evaluate to 10 instead of its true mathematical value? Give me one or two hypotheses I can test. Don't change any code yet.
### Its answer (word for word)
Because range(n - 1) stops one element early, the last coordinate x[-1] is completely ignored, leaving an uncancelled + 10 from 10 * n!
### Right, partly right, or wrong? How do you know?
 rigght since the two rastrigin coords directly printed origin 10 point , [0,1] :10 instead of 0.0 and 1.0 proving rastrigin ignored the final coordinate.
(Did it agree that the swarm was stuck in a local minimum? What did your experiment show?)
