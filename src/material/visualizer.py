import matplotlib.pyplot as plt
import numpy as np

def visualize(y_points : np.ndarray, min_: int, max_: int, step_width: float = 0.1, linear: bool = True, fix: bool = True) -> None:
    x_points = np.array([])
    for i in np.arange(min_, max_ + step_width, step_width):
        x_points = np.append(x_points, i)
    plt.plot(x_points, y_points, linestyle='solid', color='red')
    if linear:
        plt.xscale('linear')
        plt.yscale('linear')
    if fix:
        ax = plt.gca()
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    plt.show()
