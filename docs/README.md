# Geometric Lib

## Description

**Geometric Lib** is a Python library designed for basic geometric calculations. It provides functions to compute the area and perimeter (or circumference) of standard geometric shapes:

* **Circle** (`circle.py`)
* **Rectangle** (`rectangle.py`)
* **Square** (`square.py`)
* **Triangle** (`triangle.py`)

All functions use standard Python type hints, and mathematical constants are sourced from the built-in `math` module.

---

## Function Descriptions and Call Examples

### 1. Circle (`circle.py`)

#### `area(r: float) -> float`

Calculates the area of a circle using the formula: $S = \pi r^2$.

* **Parameters:** `r` — radius of the circle.
* **Returns:** Area of the circle.

**Example:**

```python
from circle import area

res = area(5)
print(res)  # 78.53981633974483
```

#### `perimeter(r: float) -> float`

Calculates the perimeter (circumference) of a circle using the formula: $P = 2\pi r$.

* **Parameters:** `r` — radius of the circle.
* **Returns:** Circumference of the circle.

**Example:**

```python
from circle import perimeter

res = perimeter(5)
print(res)  # 31.41592653589793
```

---

### 2. Rectangle (`rectangle.py`)

#### `area(a: float, b: float) -> float`

Calculates the area of a rectangle using the formula: $S = a \times b$.

* **Parameters:**
  * `a` — length of side a.
  * `b` — length of side b.
* **Returns:** Area of the rectangle.

**Example:**

```python
from rectangle import area

res = area(4, 5)
print(res)  # 20.0
```

#### `perimeter(a: float, b: float) -> float`

Calculates the perimeter of a rectangle using the formula: $P = 2 \times (a + b)$.

* **Parameters:**
  * `a` — length of side a.
  * `b` — length of side b.
* **Returns:** Perimeter of the rectangle.

**Example:**

```python
from rectangle import perimeter

res = perimeter(4, 5)
print(res)  # 18.0
```

---

### 3. Square (`squre.py`)

#### `area(a: float) -> float`

Calculates the area of a square using the formula: $S = a^2$.

* **Parameters:** `a` — length of the side.
* **Returns:** Area of the square.

**Example:**

```python
from squre import area

res = area(6)
print(res)  # 36.0
```

#### `perimeter(a: float) -> float`

Calculates the perimeter of a square using the formula: $P = 4a$.

* **Parameters:** `a` — length of the side.
* **Returns:** Perimeter of the square.

**Example:**

```python
from squre import perimeter

res = perimeter(6)
print(res)  # 24.0
```

---

### 4. Triangle (`triangle.py`)

#### `area(a: float, h: float) -> float`

Calculates the area of a triangle given its base and height using the formula: $S = \frac{a \times h}{2}$.

* **Parameters:**
  * `a` — length of the base side.
  * `h` — height drawn to the base side `a`.
* **Returns:** Area of the triangle.

**Example:**

```python
from triangle import area

res = area(8, 5)
print(res)  # 20.0
```

#### `perimeter(a: float, b: float, c: float) -> float`

Calculates the perimeter of a triangle using the formula: $P = a + b + c$.

* **Parameters:**
  * `a`, `b`, `c` — lengths of the three sides.
* **Returns:** Perimeter of the triangle.

**Example:**

```python
from triangle import perimeter

res = perimeter(3, 4, 5)
print(res)  # 12.0
```

---

## Project Change Log

* `4a49223` - fix: correct formula for rectangle perimeter and add triangle.py
* `cba684d` - feat: add a new file for working with a rectangle
* `d078c8d` - L-03: Docs added
* `8ba9aeb` - L-03: Circle and square added
