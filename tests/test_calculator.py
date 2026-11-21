import math
from calculator import calculate_probability


def test_no_predictors():
    got = calculate_probability(False, False, False, False)
    assert math.isclose(got["probability_percent"], 4.7843, abs_tol=0.01)


def test_all_predictors():
    got = calculate_probability(True, True, True, True)
    assert math.isclose(got["probability_percent"], 92.0688, abs_tol=0.01)


def test_atrial_fibrillation_only():
    got = calculate_probability(False, True, False, False)
    assert math.isclose(got["probability_percent"], 16.8133, abs_tol=0.01)
