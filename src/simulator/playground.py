from importlib.util import LazyLoader

import numpy as np

def rotation_matrix(angle_deg):
    Tetta = np.radians(angle_deg)
    T = np.array([
        [np.cos(Tetta), -np.sin(Tetta)],
        [np.sin(Tetta), np.cos(Tetta)]
    ])
    return T

def transform_matrix(angle_deg, tx, ty):
    T = np.eye(3)  # единичная матрица 3×3
    T[:2, :2] = rotation_matrix(angle_deg)  # вставить матрицу поворота в верхний левый угол
    T[0, 2] = tx  # сдвиг по x
    T[1, 2] = ty  # сдвиг по y
    return T

def forward_kinematics(link_lengths, angles_deg):
    T_total = np.eye(3)
    points = []
    for length, angle in zip(link_lengths,angles_deg):
        tx = length*np.cos(np.radians(angle))
        ty = length*np.sin(np.radians(angle))
        T = transform_matrix(angle, tx, ty)
        T_total = T_total @ T
        x_coordinates = T_total[0,2]
        y_coordinates = T_total[1, 2]
        points.append((x_coordinates,y_coordinates))
    return points

print(forward_kinematics([1,1,1], [90,1,1]))

L =[('a','b'),('c','d'),('a','b')]
for i1, i2 in L:
    print(i1,i2)