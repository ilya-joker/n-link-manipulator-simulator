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


def jacobian(link_lengths, angles_deg):
    n = len(link_lengths)
    J = np.zeros((2, n))  # матрица 2×n

    # для каждого сустава i считаем столбец якобиана
    for i in range(n):
        # суммируем вклад всех звеньев от i до конца
        for k in range(i, n):
            cumulative_angle = sum(angles_deg[:k + 1])
            J[0, i] += -link_lengths[k]*np.sin(np.radians(cumulative_angle))  # dx/dθᵢ
            J[1, i] += link_lengths[k]*np.cos(np.radians(cumulative_angle))  # dy/dθᵢ

    return J

def inverse_kinematics(link_lengths, angles_deg, target, max_iterations=1000, tolerance=1e-3):
    angles_deg = np.array(angles_deg, dtype=float)
    points = forward_kinematics(link_lengths, angles_deg)
    for i in range(max_iterations):
        target_x, target_y = target[0], target[1]
        current_x, current_y = points[-1]
        error = (target_x - current_x, target_y - current_y)
        if np.linalg.norm(error) < tolerance:
            break
        # считаем Якобиан
        J = jacobian(link_lengths, angles_deg)

        # считаем изменение углов через псевдообратную матрицу
        delta_theta = np.linalg.pinv(J) @ np.array(error)

        # обновляем углы (delta_theta в радианах — переводим в градусы)
        angles_deg = angles_deg + np.degrees(delta_theta)

        # пересчитываем позицию для следующей итерации
        points = forward_kinematics(link_lengths, angles_deg)

    return angles_deg  # возвращаем найденные углы

