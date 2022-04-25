import math

PI = 3.141592

def circle_cord(theta, radius):
    x = radius*math.cos(theta)
    y = radius*math.sin(theta)
    return (x,y)

def circle_points(radius, triangle_count):
    angle = (2*PI)/triangle_count

    points = []
    for i in range(0, triangle_count):
        theta = angle*i
        theta_n = 0
        if i+1 == triangle_count:
            theta_n = 2*PI
        else:
            theta_n = (i+1)*angle

        vertex0 = circle_cord(theta, radius)
        vertex1 = circle_cord(theta_n, radius)
        points.append((0,0))
        points.append(vertex0)
        points.append(vertex1)

    return points