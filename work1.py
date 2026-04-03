class Students:
    def __init__(self, name, surname, age,grades) ->None:
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, вік: {self.age}"

    def show_grades(self):
        return f"Оцінки: {', '.join(map(str, self.grades))}" if self.grades else "Оцінок поки немає."

    def add_grade(self, grade):
        self.grades.append(grade)




class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def show_info(self):
        return f"Бренд: {self.brand}, Модель: {self.model}, Швидкість: {self.speed} км/год, Рік: {self.year}"





def main_menu():
    student = Students("Ружицький", "Данило", 19)
    car = Car("BMW", "BMW M4 CSL (G82)", 180, 2020)

    while True:
        print("\n--- Менюшка ---")
        print("1. Показати інфу про студента")
        print("2. Додати оцінку студенту")
        print("3. Показати оцінки студента")
        print("4. Показати інформацію про авто")
        print("5. Вихід")
        choice = input("Виберіть опцію")
        match choice:
            case"1":
                print(student)
            case"2":
                grade = input("Введіть оцінку ")
                if grade.isdigit():
                    student.add_grade(int(grade))
                else:
                    print("Оцінка має бути числом")
            case"3":
                print(student.show_grades())
            case "4":
                print(car.show_info())
            case"5":
                print("кінець програми")
                break
            case _:
                print("Невірний вибір")



if __name__ == "__main__":
    main_menu()
