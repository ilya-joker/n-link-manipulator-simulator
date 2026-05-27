from simulator.config import DEFAULT_LINKS_LENGTH, DEFAULT_ANGLES
from simulator.kinematics import forward_kinematics
from simulator.visualizer import draw_manipulator


def main():
    points = forward_kinematics(DEFAULT_LINKS_LENGTH,DEFAULT_ANGLES)
    draw_manipulator(points)

if __name__ == "__main__":
    main()