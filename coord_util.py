import math


def get_coords(x, y, alpha, delta_x=0.0, delta_y=0.0, ):
    return [int(x + delta_x * math.cos(to_rad(alpha)) - delta_y * math.sin(to_rad(alpha))),
            int(y + delta_y * math.cos(to_rad(alpha)) + delta_x * math.sin(to_rad(alpha)))]


def to_rad(degree):
    return degree * math.pi / 180


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
