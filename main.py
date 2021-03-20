import turtle, math as maths, time

t = turtle.Turtle()
# turtle settings
t.speed(0)
t.hideturtle()

# the Object base class, contains the corner points and the points
# that form the faces for the model d
class Object:
    verticies = []
    faces = []

# a cube object
class Cube(Object):
    verticies = [
    #    X, Y, Z coordinates
        (-25, -25, -25),
        (25, -25, -25),
        (25, 25, -25),
        (-25, 25, -25),
        (-25, -25, 25),
        (25, -25, 25),
        (25, 25, 25),
        (-25, 25, 25)
    ]

    faces = [
    #   p1, p2, p3
        (0, 1, 3), (1, 2, 3),
        (0, 1, 5), (0, 4, 5),
        (3, 0, 4), (3, 7, 4),
        (2, 3, 7), (2, 6, 7),
        (1, 2, 6), (1, 5, 6),
        (4, 5, 7), (5, 6, 7)
    ]

# a pyramid object
class pyramid(Object):
    verticies = []
    faces = []

# a camera object, contains the position in the 3d space
# class Camera():
#     def __init__(self, position):
#         self.x, self.y, self.z = position


# project the points from the 3d space to the 2d screen 
def projection(vec3d, k1, k2):
    result = []
    length = len(vec3d)
    for i in range(length):
        x, y, z = vec3d[i]
        result.append((k1 * x / (k2 + z), k1 * y / (k2 + z)))
    return result

# rotate the points in the 3D space with respect to the x, y, and z axis
# def rotation(vec3d, rotX, rotY, rotZ, camera):
def rotation(vec3d, rotX, rotY, rotZ):
    result = []
    length = len(vec3d)
    for i in range(length):
        x, y, z = vec3d[i]
        # x -= camera.x
        # y -= camera.y
        # z -= camera.z

        i = (x*maths.cos(rotX)*maths.cos(rotY)) + (y*maths.sin(rotX)*maths.cos(rotY)) - (z*maths.sin(rotY))

        j = (x * (maths.cos(rotX)*maths.sin(rotY)*maths.sin(rotZ) - maths.sin(rotX)*maths.cos(rotZ))) + (y * (maths.sin(rotX)*maths.sin(rotY)*maths.sin(rotZ) + maths.cos(rotX)*maths.cos(rotZ))) + (z * maths.cos(rotY) * maths.sin(rotZ))

        k = (x * (maths.cos(rotX)*maths.sin(rotY)*maths.cos(rotZ) + maths.sin(rotX)*maths.sin(rotZ))) + (y * (maths.sin(rotX)*maths.sin(rotY)*maths.cos(rotZ) - maths.cos(rotX)*maths.sin(rotZ))) + (z * maths.cos(rotY) * maths.cos(rotZ))

        result.append((i, j, k))

    return result

# draw a line from point 1 to point 2 using the triangles of the model
def drawLine(vec2d, faces):
    length = len(faces)
    for i in range(length):
        r1, r2, r3 = faces[i]
        p1 = vec2d[r1]
        p2 = vec2d[r2]
        p3 = vec2d[r3]
        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)

# use turtle to draw out the points in the 2D vector
def drawDot(vec2d):
    length = len(vec2d)
    for i in range(length):
        x, y = vec2d[i]
        t.penup()
        t.goto(x, y)
        t.dot(5)
        t.pendown()


if __name__ == '__main__':
    # initialize a cube object 
    dirt = Cube()
    # the coordinates of the camera (default 0, 0, 0)
    # camera = Camera((0, 0, 0))
    vec2d = []
    vec3d = []

    width, height = turtle.screensize()
    # the distance between the object and the viewer
    k2 = 70
    # the distance between the object and the screen
    k1 = width * k2 * 3 / 8 / 50
    # initial rotation angle
    rotX, rotY, rotZ = 0, 0, 0

    while True:
        t.clear()

        # vec3d = rotation(dirt.verticies, rotX, rotY, rotZ, camera)
        vec3d = rotation(dirt.verticies, rotX, rotY, rotZ)

        vec2d = projection(vec3d, k1, k2)
        drawDot(vec2d)
        drawLine(vec2d, dirt.faces)

        rotX = rotX + 0.1
        rotY = rotY + 0.1
        #rotZ = rotZ + 0.1
        time.sleep(0.3)


# create a cube object that contains the verticies of each points in a 3D space
# rotate the coordinates of the points using rotation matricies
# convert the points from 3d points into 2D points
# use turtle to draw out the points on the screen
# use turtle to draw out the lines that connect the points, use the triangle points set

# repeat