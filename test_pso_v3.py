"""Tests for pso_v3.py. Run from this folder: pytest"""
import numpy as np

from pso_v3 import Particle, pso_get_best, run_pso
from pso_v3 import Particle, pso_get_best, run_pso, rastrigin

def test_booth_finds_minimum():
    x, value, history = run_pso("booth", 2, 20, -10, 10, 100)
    assert np.allclose(x, [1, 3], atol=1e-4)
    assert value < 1e-8


def test_one_iteration():
    """Issue 1: max_iter = 1 raised UnboundLocalError."""
    x, value, history = run_pso("booth", 2, 20, -10, 10, 1)
    assert len(history) == 1


def test_runs_every_iteration():
    """Issue 1: 30 iterations asked for, 29 run."""
    x, value, history = run_pso("booth", 2, 20, -10, 10, 30)
    assert len(history) == 30


def swarm_with(values):
    """Particles whose fitness values are the given numbers."""
    swarm = [Particle(2, 0, 1) for _ in values]
    for p, value in zip(swarm, values):
        p.set_fitness(value)
    return swarm


def test_tie_in_the_middle():
    """Issue 2: a tie for the lowest value gave the particle after it."""
    assert pso_get_best(swarm_with([3.0, 1.0, 1.0, 5.0])) == 2


def test_tie_at_the_end():
    """Issue 2: a tie at the last particle gave an index past the end."""
    assert pso_get_best(swarm_with([3.0, 1.0, 1.0])) == 2

def test_get_pbest():
    """Issue 3: get_pbest raised AttributeError."""
    p = Particle(2, -10, 10)
    assert np.array_equal(p.get_pbest(), p.pbest)

def test_sphere_zero_bound_early_stop():
    """Issue 4: sphere on [0, 10] crashed with ZeroDivisionError and should stop early."""
    x, value, history = run_pso("sphere", 2, 20, 0, 10, 100)
    assert value == 0.0
    assert len(history) < 100    

def test_rastrigin_known_value_and_symmetry():
    """Issue 5: rastrigin ignored the last coordinate due to range(n - 1)."""
    assert rastrigin([0.0, 0.0]) == 0.0
    assert np.isclose(rastrigin([0.0, 1.0]), 1.0)
    assert np.isclose(rastrigin([1.5, -2.5]), rastrigin([-1.5, 2.5]))  