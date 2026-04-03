import math



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Коло з радіусом {self.radius}"





class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Прямокутник {self.width}x{self.height}"





class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimetr(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Трикутник зі сторонами {self.a}, {self.b}, {self.c}"







def geometry_menu():
    while True:
        print("\n---менюшка ---")
        print("1. Коло")
        print("2. Прямокутник")
        print("3. Трикутник")
        print("4. Вихід")
        choice = input("Оберіть фігуру: ")
        match choice:
            case "1":
                r = float(input("Введіть радіус: "))
                circle = Circle(r)
                print(circle)
                print(f"Площа: {circle.area():.2f}")
                print(f"Периметр: {circle.perimetr():.2f}")
            case"2":
                w = float(input("Ширина: "))
                h = float(input("Висота: "))
                rect = Rectangle(w, h)
                print(rect)
                print(f"Площа: {rect.area():.2f}")
                print(f"Периметр: {rect.perimetr():.2f}")
            case "3":
                a = float(input("Сторона a: "))
                b = float(input("Сторона b: "))
                c = float(input("Сторона c: "))
                if a + b > c and a + c > b and b + c > a:
                    tri = Triangle(a, b, c)
                    print(tri)
                    print(f"Площа: {tri.area():.2f}")
                    print(f"Периметр: {tri.perimetr():.2f}")
                else:
                    print("Такий трикутник не існує.")
            case"4":
                print("Завершення програми.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    geometry_menu()
