class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def Area(self):
            print("I am a: " + self.name + "\n"+ "I have " + self.side + " sides")

obj_shape=Shapes("shape", "so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1,wid1):
        self.length = len1
        self.width = wid1
    def Area(self):
        result = self.length * self.width
        return result
obj_book = Rectangle(10,7)
obj_screen=Rectangle(5,7)
print("The area of a book is: " + str(obj_book.Area()))
print("The area of a screen is: " + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self, rad1):
        self.radius = rad1
    def Area(self):
        result = 3.14159 * int(self.radius^ 2)
        return result
obj_circle=Circle(10)
print("The area of a circle is: " + str(obj_circle.Area()))

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def Area(self):
        result = (0.5 * self.base * self.height)
        return result
obj_tri = Triangle(5,6)
print("The area of a triangle is: " + str(obj_tri.Area()))
