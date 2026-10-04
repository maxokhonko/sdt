def area(a: float, h: float) -> float:
    """Calculates the area of a triangle given side a and height h.

    Example:
        area(8, 5)  # 20.0
    """
    return a * h / 2


def perimeter(a: float, b: float, c: float) -> float:
    """Calculates the perimeter of a triangle with sides a, b, and c.

    Example:
        perimeter(3, 4, 5)  # 12.0
    """
    return a + b + c