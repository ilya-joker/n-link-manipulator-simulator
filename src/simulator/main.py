from simulator.config import DEFAULT_LINKS_LENGTH, DEFAULT_ANGLES
from simulator.kinematics import forward_kinematics, inverse_kinematics
from simulator.visualizer import draw_manipulator


def main():
    target = (2.0, 1.0)
    angles_deg = inverse_kinematics(DEFAULT_LINKS_LENGTH, DEFAULT_ANGLES, target, max_iterations=1000, tolerance=1e-3)
    points = forward_kinematics(DEFAULT_LINKS_LENGTH,angles_deg)
    draw_manipulator(points,DEFAULT_LINKS_LENGTH, target )

if __name__ == "__main__":
    main()