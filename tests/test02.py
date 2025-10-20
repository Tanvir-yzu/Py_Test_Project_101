import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

# 1. Boundary and Exception Handling Tests

def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_large_number_operations(calc):
    large = 1e18
    assert calc.add(large, large) == 2e18
    assert calc.multiply(large, 2) == 2e18
    assert calc.divide(large, 2) == large / 2


def test_negative_and_zero_operations(calc):
    assert calc.add(-5, 0) == -5
    assert calc.subtract(0, -5) == 5
    assert calc.multiply(-3, 0) == 0
    assert calc.divide(0, 1) == 0

# 2. Comparative Function Tests

def test_comparative_maximum(calc):
    assert calc.maximum(10, 20) == 20
    assert calc.maximum(-1, -2) == -1
    assert calc.maximum(0, 0) == 0


def test_comparative_minimum(calc):
    assert calc.minimum(10, 20) == 10
    assert calc.minimum(-1, -2) == -2
    assert calc.minimum(0, 0) == 0

# 3. State Management Tests

def test_last_answer_updates(calc):
    calc.add(1, 2)
    assert calc.last_answer == 3
    calc.subtract(calc.last_answer, 1)
    assert calc.last_answer == 2
    calc.multiply(calc.last_answer, 5)
    assert calc.last_answer == 10
    calc.divide(calc.last_answer, 2)
    assert calc.last_answer == 5


def test_last_answer_not_updated_on_error(calc):
    calc.add(2, 2)
    assert calc.last_answer == 4
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
    assert calc.last_answer == 4

# 4. Parameterized Tests

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 5, 4),
    (1.5, 2.5, 4.0),
    (0, 0, 0),
    (-3, 0, -3),
    (100, -0.5, 99.5),
])
def test_add_param(calc, a, b, expected):
    assert calc.add(a, b) == expected
    assert calc.last_answer == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 5, -5),
    (2.5, 0.5, 2.0),
    (-1, -2, 1),
    (3, -5, 8),
])
def test_subtract_param(calc, a, b, expected):
    assert calc.subtract(a, b) == expected
    assert calc.last_answer == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, -2, 2),
    (1.5, 2, 3.0),
    (0, 123, 0),
    (-4, 2.5, -10.0),
])
def test_multiply_param(calc, a, b, expected):
    assert calc.multiply(a, b) == expected
    assert calc.last_answer == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2.0),
    (7, 2, 3.5),
    (-8, 2, -4.0),
    (-9, -3, 3.0),
    (9, -3, -3.0),
    (1, 3, 1/3),
    (0, 5, 0.0),
])
def test_divide_param(calc, a, b, expected):
    assert calc.divide(a, b) == expected
    assert calc.last_answer == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 5),
    (5, 5, 5),
    (-1, -2, -1),
    (3.5, 2.2, 3.5),
])
def test_maximum_param(calc, a, b, expected):
    assert calc.maximum(a, b) == expected
    assert calc.last_answer == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 3),
    (5, 5, 5),
    (-1, -2, -2),
    (3.5, 2.2, 2.2),
])
def test_minimum_param(calc, a, b, expected):
    assert calc.minimum(a, b) == expected
    assert calc.last_answer == expected