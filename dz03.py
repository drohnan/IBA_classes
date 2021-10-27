"""
Создать класс – Треугольник, заданного тремя точками. Функции-члены изменяют точки,
обеспечивают вывод на экран координат, рассчитывают длины сторон и периметр треугольника.
Создать список объектов.
a) подсчитать количество треугольников разного типа (равносторонний,	равнобедренный,	прямоугольный, произвольный).
b) определить для каждой группы наибольший и наименьший по периметру объект.
"""


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def __str__(self):
        return f"\nТреугольник:\nТочка А с координатами ({self.x1}; {self.y1})\nТочка В с координатами ({self.x2}; {self.y2})\nТочка С с координатами ({self.x3}; {self.y3}) "

    def lengths(self):
        a = round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)
        b = round(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5, 2)
        c = round(((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5, 2)
        return a, b, c

    def perimeter(self):
        a = round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)
        b = round(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5, 2)
        c = round(((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5, 2)
        return a + b + c

    def is_ravnostor(self):
        a = round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)
        b = round(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5, 2)
        c = round(((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5, 2)
        return a == b == c

    def is_ravnobedr(self):
        a = round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)
        b = round(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5, 2)
        c = round(((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5, 2)
        return a == b or b == c or a == c
    def is_priamoug(self):
        a = round(((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5, 2)
        b = round(((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5, 2)
        c = round(((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5, 2)
        return (c ** 2 == a ** 2 + b ** 2) or (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2)


tr1 = Triangle(0, 0, 0, 3, 4, 3)  # прямоугольный
tr2 = Triangle(0, 0, 0, 5, 5, 0)  # прямоугольный  равнобедренный 
tr3 = Triangle(6, 5, 3, 7, -6, 12)  # наверное произвольный :)
tr4 = Triangle(7, 3, 4, 6, 2, 56) # наверное произвольный :)

triangles = [tr1, tr2, tr3, tr4]
print(*triangles)

kolvo_ravnostor = 0
ravnostor_triangles = []
kolvo_ravnobedr = 0
ravnobedr_triangles = []
kolvo_priamoug = 0
priamoug_triangles = []
kolvo_proizv = 0
proizv_triangles = []
for i in range(len(triangles)):
    if triangles[i].is_ravnostor():
        kolvo_ravnostor += 1
        ravnostor_triangles.append(triangles[i].perimeter())
    elif triangles[i].is_ravnobedr():
        kolvo_ravnobedr += 1
        ravnobedr_triangles.append(triangles[i].perimeter())
    elif triangles[i].is_priamoug():
        kolvo_priamoug += 1
        priamoug_triangles.append(triangles[i].perimeter())
    else:
        kolvo_proizv += 1
        proizv_triangles.append(triangles[i].perimeter())

print(f"Количество равносторонних треугольников = {kolvo_ravnostor}, периметр наименьшего треугольника = {min(ravnostor_triangles)}, периметр наибольшего треугольника = {max(ravnostor_triangles)}" if ravnostor_triangles != [] else "Равносторонних треугольников нет")
print(f"Количество равнобедренных треугольников = {kolvo_ravnobedr}, периметр наименьшего треугольника = {min(ravnobedr_triangles)}, периметр наибольшего треугольника = {max(ravnobedr_triangles)}" if ravnobedr_triangles != [] else "Равнобедренных треугольников нет")
print(f"Количество прямоугольных треугольников = {kolvo_priamoug}, периметр наименьшего треугольника = {min(priamoug_triangles)}, периметр наибольшего треугольника = {max(priamoug_triangles)}" if priamoug_triangles != [] else "Прямоугольных треугольников нет")
print(f"Количество произвольных треугольников = {kolvo_proizv}, периметр наименьшего треугольника = {min(proizv_triangles)}, периметр наибольшего треугольника = {max(proizv_triangles)}" if proizv_triangles != [] else "Произвольных треугольников нет")

