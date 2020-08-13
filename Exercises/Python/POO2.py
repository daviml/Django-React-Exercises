class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def bark(self):
        print("WOOF")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()