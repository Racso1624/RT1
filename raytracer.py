from math import *
from sphere import *
from vector import *
from gl import *

class RayTracer(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_color = setColor(0, 0, 0)
        self.current_color = setColor(1, 1, 1)
    
    def clear(self):
        self.frambuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
        ]
    
    def point(self, x, y, c = None):
        if y >= 0 and y < self.height and x > 0 and x < self.width:
            self.frambuffer[y][x] = c or self.current_color

    def write(self, filename):
        glFinish(filename)

    def cast_ray(self, origin, direction):
        s = Sphere(V3(-3, 0, 16), 2)

        if s.ray_intersect(origin, direction):
            return setColor(1, 0, 0)
        else:
            self.clear_color

    def render(self):
        fov = int(pi/2)
        ar = self.width / self.height
        tana = tan(fov / 2)
        for y in range(self.height):
            for x in range(self.width):
                i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                j = (1 - (2 * (y + 0.5) / self.height)) * tana

                direction = V3(i, j, -1).norm()
                origin = V3(0, 0, 0)
                c = cast_ray(origin, direction)

r = RayTracer(800, 600)
r.clear()
r.point(100, 100)
r.render()
r.write