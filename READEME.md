# Project 101 — Calculator with PyTest

A simple Python `Calculator` class with a comprehensive PyTest suite. The calculator tracks the last computed result via `last_answer`.

## Features
- Basic ops: `add`, `subtract`, `multiply`, `divide`
- Helpers: `maximum`, `minimum`
- `last_answer` property updated after every successful operation
- PyTest suite with extensive edge cases and coverage support

## Files
- `calculator.py` — Calculator implementation
- `tests/test_calculator.py` — PyTest suite
- `.gitignore` — Ignores caches, coverage outputs, and virtual environments

## Requirements
- Python 3.12+ recommended
- Optional: `pytest` and `coverage` for tests and reports

## Setup (optional virtual environment)
Create a virtual environment:

```bash
python -m venv myenv
```

Activate it (Windows):

```bash
myenv\Scripts\activate
```

Install test tools:

```bash
pip install -U pytest coverage
```

## Run Tests
Execute the full test suite:

```bash
python -m pytest -q
```

Run a single test:

```bash
python -m pytest -q tests\test_calculator.py::test_add
```

## Coverage Report
Generate coverage data:

```bash
coverage run -m pytest -q
```

Create HTML report:

```bash
coverage html
```

Open the report at `htmlcov\index.html`.

## Usage Example

```python
from calculator import Calculator

calc = Calculator()

print(calc.add(2, 3))        # 5
print(calc.last_answer)      # 5

print(calc.multiply(4, 2))   # 8
print(calc.last_answer)      # 8

print(calc.divide(7, 2))     # 3.5
print(calc.maximum(10, 7))   # 10
print(calc.minimum(3, 5))    # 3
```

## Notes
- `divide` raises `ZeroDivisionError` on division by zero and preserves `last_answer`.
- The test suite includes combinations of zeros, negatives, and floats.
- If you want to track coverage outputs in git, remove `htmlcov/` from `.gitignore`.