from material import calculate_data_points, visualize
import numpy as np

def vis_f(f: str, min_: int, max_: int, step: float = 0.1, linear: bool = True, fix: bool = True):
    res: np.ndarray = calculate_data_points(f, min_, max_, step)
    visualize(res, min_, max_, step, linear, fix)

def manual_visualization():
    f = input("Please input the function: ")
    min_ = int(input("Please input the lower bound: "))
    max_ = int(input("Please input the upper bound: "))
    step = float(input("Please input the step_width: "))
    linear = True if input("Shall the scales be linear? (y/n): ") == "y" else False
    fix = True if input("Shall the axis be fixed at 0? (y/n): ") == "y" else False
    res : np.ndarray = calculate_data_points(f, min_, max_, step)
    visualize(res, min_, max_, step, linear, fix)

if __name__ == "__main__":
    manual_visualization()