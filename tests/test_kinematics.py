import numpy as np

from simulator.kinematics import forward_kinematics, inverse_kinematics, jacobian


def test_forward_kinematics_horizontal():
    link_lengths = [1, 1]
    angles_deg = [0, 0]
    expected = (2, 0)
    result  = forward_kinematics(link_lengths, angles_deg)
    assert np.allclose(result[-1], expected, atol=1e-3) #atol - absolute tolerance

def test_fk_vertical():
    link_lengths = [1, 1]
    angles_deg = [90, 0]
    expected = (0, 2)
    result = forward_kinematics(link_lengths, angles_deg)
    assert np.allclose(result[-1], expected, atol=1e-3)  # atol - absolute tolerance

def test_fk_three_links_horizontal():
    link_lengths = [1, 1, 1]
    angles_deg = [0, 0, 0]
    expected = (3, 0)
    result = forward_kinematics(link_lengths, angles_deg)
    assert np.allclose(result[-1], expected, atol=1e-3)


def test_ik_reaches_target():
    link_lengths = [1, 1, 1]
    start_angles = [10, 10, 10]
    target = (2.0, 1.0)
    result_angles = inverse_kinematics(link_lengths, start_angles, target)
    # проверяем что FK с найденными углами даёт целевую точку
    end_effector = forward_kinematics(link_lengths, result_angles)[-1]
    assert np.allclose(end_effector, target, atol=1e-3)

def test_jacobian_shape():
    link_lengths = [1, 1, 1]
    angles_deg = [0, 0, 0]
    J = jacobian(link_lengths, angles_deg)
    assert J.shape == (2, 3)
