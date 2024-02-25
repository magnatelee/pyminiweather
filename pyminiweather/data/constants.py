from enum import Enum


class Constants(float, Enum):
    hv_beta = 0.05

    p0 = 1.0e5
    C0 = 27.5629410929725921310572974482
    gamma = 1.40027894002789400278940027894
    grav = 9.8

    cp = 1004.0
    cv = 717.0
    rd = 287

    pi = 3.14159265358979323846264338327

    theta0 = 300.0  # Surface-level Exner pressure
    exner0 = 1.0  # Background potential temperature
