#Example of Overloading
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))        
print(m.add(5, 10))    
print(m.add(5, 10, 15))  

#Example of Overriding
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog()
print(d.sound())   


class Student:
    # Default constructor
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
# Using default constructor
s = Student()
# print(s.name, s.age)

class Person:
    # Parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Using parameterized constructor
p = Person("Prakriti", 18)
print(p.name, p.age)

