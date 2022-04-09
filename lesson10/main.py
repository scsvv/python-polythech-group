'''
    class - описание нашего объекта у нас хранятся, его поля (переменные) и его методы (функции)
    object - это уже екземпляр, существующий объект, который имеет значения для полей и может запускать методы

    __init__ - создает представление и дает значение полям
    self - ссылка на объкет, который делает вызов.
    super() - ссылка на класс родителя
'''
class OwnMath:
    def __init__(self):
        self.pi = 3.14

    def sum(self, a, b): 
        return a + b
    
    def minus(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b
    
    def obb(self, a, b):
        return a / b

    def squard(self, a):
        return self.multi(a, a)

class OwnGeometry(OwnMath):

    def __init__(self):
        super().__init__()

class OwnCyrcle(OwnGeometry):
    def __init__(self, r):
        self.radius = r
        self.diametr_value = self.diametr()
        super().__init__()
    
    def diametr(self):
        return self.multy(2, self.radius)
    
    def cyrcle_squad(self):
        return self.multi(self.pi, self.radius * self.radius)

class OwnQuadrangular(OwnGeometry):

    def __init__(self, A, B, C, D, AB, BC, CD, AD):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = AB
        self.BC = BC
        self.CD = CD
        self.AD = AD
        super().__init__()
    
    def perimetr(self):
        return self.A + self.B + self.C + self.D
    
    def square(self):
        pass
    
class OwnRightQuadrangular(OwnQuadrangular):
    def __init__(self, A, B):
        super().__init__(A, B, A, B, 90, 90, 90, 90)
    
    def square(self):
        return self.A * self.B

class OwnSquare(OwnQuadrangular):
    def __init__(self, A):
        super().__init__(A, A, A, A, 90, 90, 90, 90)

    def square(self):
        return self.A ** 2


own_math = OwnMath()
own_geometry = OwnGeometry()
cyrcle_1 = OwnCyrcle(1)
cyrcle_2 = OwnCyrcle(2)
cyrcle_3 = OwnCyrcle(3)
q1 = OwnRightQuadrangular(3, 4)
q2 = OwnSquare(4) 
