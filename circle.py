import math


def area(r: float) -> float:
    """Calculates the area of a circle with radius r.

    Example:
        area(5)  # 78.53981633974483
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """Calculates the perimeter of a circle with radius r.

    Example:
        perimeter(5)  # 31.41592653589793
    """
    return 2 * math.pi * r
