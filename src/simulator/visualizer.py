from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from simulator.math_utils import calculate_workspace_bounds


def draw_workspace(ax, r_max, r_min):
    outer = Circle((0, 0), r_max, fill=False, linestyle="--", color="gray", label="Max reach")
    ax.add_patch(outer)

    if r_min > 0:
        inner = Circle((0, 0), r_min, fill=False, linestyle=":", color="gray", label="Min reach")
        ax.add_patch(inner)

def draw_manipulator(points,link_lengths, target=None):
    # Create figure and axes objects
    fig, ax = plt.subplots(figsize=(8, 8))
    r_max, r_min = calculate_workspace_bounds(link_lengths)
    draw_workspace(ax, r_max, r_min)
    if target is not None:
        ax.plot(target[0], target[1], "g*", markersize=15, label="Target")
    # Start from the origin (0, 0) and add all joint positions
    X = [0]
    Y = [0]
    for x, y in points:
        X.append(x)
        Y.append(y)

    # Draw all links as a single connected line with joint markers
    ax.plot(X, Y, "o-r", label="Links")

    # Calculate plot limits based on the furthest point
    max_reach = max(max(abs(x) for x, y in points), max(abs(y) for x, y in points))
    margin = 0.5

    # Set equal axis limits with margin so the manipulator is centered
    ax.set_xlim(-max_reach - margin, max_reach + margin)
    ax.set_ylim(-max_reach - margin, max_reach + margin)

    # Keep equal scale on X and Y to prevent distortion
    ax.set_aspect("equal", adjustable="box")

    # Draw reference axes
    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)
    ax.grid(True)
    ax.legend()
    ax.set_title("N-Link Manipulator")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")


    plt.show()
