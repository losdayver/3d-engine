import math
import numpy as np
import pygame as pg
from mesh import *

pg.init()

screen = pg.display.set_mode((800, 800))

title = 'снеговичок пляшет'

w = screen.get_width()
h = screen.get_height()
zfar = 1000.0
znear = 0.1
fov = math.radians(30)

a = h/w
f = 1/math.tan(fov/2)
q = zfar/(zfar-znear)

proj_mat = np.empty([4, 4], dtype = np.float64)
proj_mat[0, 0] = a * f
proj_mat[1, 1] = f
proj_mat[2, 2] = q
proj_mat[2, 3] = 1
proj_mat[3, 2] = -znear * q

mesh1 = mesh()
mesh1.load_from_obj('snowman.obj')

camera = np.array([0.0, 0.0, 0.0], dtype=np.float64)

while 1:
    screen.fill((0, 0, 0))

    frame_start = pg.time.get_ticks()
    t = frame_start/600

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            quit()

    tris_to_raster = []

    for tri in mesh1:
        tri_transformed = []

        for point in tri:
            point_transformed = np.array([point[0], point[1], point[2], 1], dtype=np.float64)
            #point_transformed -= np.ones(4, dtype=np.float64)*0.5

            # rot_mat_z = np.array(
            #     [[math.cos(t), -math.sin(t), 0, 0], [math.sin(t), math.cos(t), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            # rot_mat_x = np.array(
            #     [[1, 0, 0, 0], [0, math.cos(t), -math.sin(t), 0], [0, math.sin(t), math.cos(t), 0], [0, 0, 0, 1]])
            jump = abs(math.sin(t*4)*0.5)+0.5

            rot_mat_y = np.array(
                [[math.cos(t), 0, math.sin(t), 0], [0, jump, 0, 0], [-math.sin(t), 0, math.cos(t), 0], [0, 0, 0, 1]])

            #point_transformed = np.matmul(point_transformed, rot_mat_z)
            #point_transformed = np.matmul(point_transformed, rot_mat_x)
            point_transformed = np.matmul(point_transformed, rot_mat_y)

            point_transformed[2] += 4
            point_transformed[1] += 1

            point_transformed[0] += -math.sin(t)
            point_transformed[2] += math.cos(t)
            point_transformed[1] += abs(math.cos(t*2))*1.3

            tri_transformed.append(point_transformed)


        vect1 = tri_transformed[1][:3] - tri_transformed[0][:3]
        vect2 = tri_transformed[2][:3] - tri_transformed[0][:3]

        normal = np.cross(vect1, vect2)
        normal /= math.sqrt(normal[0]**2+normal[1]**2+normal[0]**2)
        vect_camera_to_normal = tri_transformed[0][:3] - camera
        dot = np.dot(normal, vect_camera_to_normal)

        if dot < 0:
            tris_to_raster.append([tri_transformed, dot])

    def sort_by(e):
        item = e[0]
        mid_point = ((item[0] + item[1]) / 2 + item[2]) / 2

        distance = camera - mid_point[:3]
        distance = math.sqrt(distance[0]**2 + distance[1]**2 + distance[2]**2)

        return distance

    tris_to_raster.sort(reverse=True, key=sort_by)

    for e in tris_to_raster:
        tri_transformed = e[0]
        tri_to_draw = []
        for point in tri_transformed:
            point_transformed = np.matmul(point, proj_mat)
            point_transformed[0] /= point_transformed[3]
            point_transformed[1] /= point_transformed[3]
            tri_to_draw.append([point_transformed[0] * 0.1 * w + w // 2, point_transformed[1] * 0.1 * h + h // 2])

        g = abs(int(64)*e[1])
        if g > 255: g = 255
        pg.draw.polygon(screen, [0, g, g], tri_to_draw)
        #pg.draw.lines(screen, [255 - g, 0, 255 - g], True, tri_to_draw, 1)

    frame_end = pg.time.get_ticks()
    pg.display.set_caption(str(math.ceil(1000/(frame_end - frame_start))))

    pg.display.flip()