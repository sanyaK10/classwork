class Animal:
    def __init__(self, name, type, sound) ->None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f"animals of type {self.type} named {self.name} makes sound:{self.sound}")

    def __str__(self) -> str:
        return f"Name : {self.name}\nType: {self.type}\nSound:{self.sound}"


animal = Animal("Buddy","dog","woof")
animal2 = Animal("Charlie","parrot","hello")

animal.make_sound()
animal2.make_sound()

number = int("10")
number = int(10.7)


# animal.make_sound()
# animal.type = "dog"
# animal2 = Animal()
# print(animal.type)
# print(animal2.type)
# print(type(animal))

# class Calculator:
#     def add(self,num1,num2):
#         return num1 + num2
    
#     def substruct(self,num1,num2):
#         return num1- num2
    
#     def multiply(self,num1,num2):
#         return num1*num2
    
#     def divide(self,num1,num2):
#         if num2 == 0: raise ZeroDivisionError()
#         return num1/num2
    
# calc = Calculator()

# print(calc.add(10,12))
# print(calc.multiply(5,5))
