import math

import numpy as np

# a = np.array([1,1,1])
#
# b = np.array([[0,0,0], [0,0,0], [0,0,0]])
# #[y, x]
# b[0, 1] = 1
#
# print(b)

# a = np.array([0,0,1])
# b = np.array([2,0,0])
# c = np.cross(np.transpose(a), b)
# c = c / math.sqrt(c[0]**2 + c[1]**2 + c[2]**2)
# print(c)

# vertices = []
# triangles = []
#
# stream = open('lamp_post.obj', 'r')
# while 1:
#      line = stream.readline()
#      if line == '': break
#      if line[0] == 'v':
#           temp = line[:-2].split(' ')[1:]
#           vertex = np.asarray(temp, dtype=np.float64)
#           vertices.append(vertex)
#      elif line[0] == 'f':
#           temp = line[:-2].split(' ')[1:]
#           v1 = vertices[int(temp[0])]
#           v2 = vertices[int(temp[0])]
#           v3 = vertices[int(temp[0])]
#           triangles.append([v1, v2, v3])
#
# print(vertices)
# print(triangles)

