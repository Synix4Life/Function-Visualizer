import numpy as np
from sympy import symbols, lambdify, sympify

__variable = symbols("x")

def calculate_data_points(f: str, min_: int, max_: int, step_width: float = 0.1) -> np.ndarray:
    res = np.array([])
    f = lambdify(__variable, sympify(f))
    for i in np.arange(min_, max_ + step_width, step_width):
        res = np.append(res, f(i))
    return res