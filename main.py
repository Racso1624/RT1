from material import *
from sphere import *
from vector import *
from gl import *
from raytracer import *

red = Material(difusse=setColor(1, 0, 0))
white = Material(difusse=setColor(1, 1, 1))
orange = Material(difusse=setColor(1, 0.5, 0))
black = Material(difusse=setColor(0, 0, 0))

r = RayTracer(1024, 1024)
r.light = Light(V3(0, 0, 0), 1)
r.scene = [
    #Nariz
    Sphere(V3(0, -0.9, -8), 0.4, orange),

    #Botones
    Sphere(V3(0, 2.8, -8), 0.4, black),
    Sphere(V3(0, 1.7, -8), 0.3, black),
    Sphere(V3(0, 0.7, -8), 0.2, black),

    #Ojos
    Sphere(V3(0.25, -1.3, -7), 0.2, black),
    Sphere(V3(-0.25, -1.3, -7), 0.2, black),

    #Boca
    Sphere(V3(-0.4, -0.4, -7), 0.1, black),
    Sphere(V3(-0.15, -0.3, -7), 0.1, black),
    Sphere(V3(0.15, -0.3, -7), 0.1, black),
    Sphere(V3(0.4, -0.4, -7), 0.1, black),

    #Cuerpo
    Sphere(V3(0, -1, -9), 1.3, white),
    Sphere(V3(0, 1, -10), 1.7, white),
    Sphere(V3(0, 3, -11), 2, white)
]
r.render()
r.write('RT1.bmp')