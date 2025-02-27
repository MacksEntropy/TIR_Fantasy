import pytest

from main import TIRFantasy

tir = TIRFantasy()

@pytest.mark.parametrize("t,expected", [
    (450, 1.067),
    (465, 1.032),
    (480, 1.000),
    (495, 0.970),
    (510, 0.941),
])
def test_speed_score(t, expected):
    assert expected == round(tir.speed_score(480, t), 3)

@pytest.mark.parametrize("t,expected", [
    (450, -0.0586),
    (465, -0.0303),
    (480, 0.0000),
    (495, 0.0322),
    (510, 0.0664),
])
def test_pace_adherence(t, expected):
    assert expected == round(tir.pace_adherence(480, t), 4)

@pytest.mark.parametrize("rank,expected", [
    (1, 100.00),
    (9, 90.86),
    (18, 80.57),
    (27, 70.29),
    (36, 60.00),
])
def test_difficulty_score(rank, expected):
    assert expected == round(tir.difficulty_score(rank), 2)

@pytest.mark.parametrize("t,expected", [
    (450, 31.06),
    (465, 28.08),
    (480, 25.00),
    (495, 21.83),
    (510, 18.55),
])
def test_performance_score(t, expected):
    assert expected == round(tir.performance_score(
        speed_score=tir.speed_score(480, t),
        pace_adherence=tir.pace_adherence(480,t),
        difficulty_score=tir.difficulty_score(1)
    ),2)

