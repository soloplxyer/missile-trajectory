from math import *

def speed(vx, vy):
    return sqrt((vx**2) + (vy**2))

def dist(x1, y1, x2, y2):
    return hypot(x2 - x1, y2 - y1)#sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angleToPoint(x1, y1, x2, y2):
    d = dist(x1, y1, x2, y2)
    dx = (x2 - x1) / d
    dy = (y2 - y1) / d

    a = acos(dx) * (180/pi);
    if dy < 0:
        a = 360 - a

    return a