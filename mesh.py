import numpy as np

class triangle:
    def __init__(self, v1, v2, v3):
        self.vertex1 = np.array(v1, dtype=np.float64)
        self.vertex2 = np.array(v2, dtype=np.float64)
        self.vertex3 = np.array(v3, dtype=np.float64)
        self._vertex_array = [self.vertex1, self.vertex2, self.vertex3]

    def __getitem__(self, item):
        return self._vertex_array[item]

class mesh:
    def __init__(self, triangles=[]):
        self.triangles = triangles

    def __getitem__(self, item):
        return self.triangles[item]

    def load_from_obj(self, file_path):
        vertices = []
        triangles = []

        stream = open(file_path, 'r')
        while 1:
            line = stream.readline()
            if line == '': break
            if line[0] == 'v':
                temp = line[:-1].split(' ')[1:]
                vertex = np.asarray(np.array(temp, dtype=str), dtype=np.float64)
                vertices.append(vertex)
            elif line[0] == 'f':
                temp = line[:-1].split(' ')[1:]
                v1 = vertices[int(temp[0])-1]
                v2 = vertices[int(temp[1])-1]
                v3 = vertices[int(temp[2])-1]
                triangles.append(triangle(v1, v2, v3))

        self.triangles = triangles