


def calculate_workspace_bounds(link_lengths):
    r_max = sum(link_lengths)
    r_min = max(0, 2*max(link_lengths) - r_max)
    return r_max, r_min