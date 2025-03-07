# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model 
#     def move(self):
#         print("Move!")
# class Car(Vehicle):
#         pass

# class Boat(Vehicle):
#         def move(self):
#             print("sail!")

# class Plane(Vehicle):
#         def move(self):
#             print("Fly!")
                  
# car1= Car("ford", "mustang")
# boat1=Boat("Ibiza", "Touring 20")
# plane1=Plane("boeing", "747")

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# class Duck:
#     def sound(self):
#         return "Quack Quack"
# class Anotherbird:
#     def sound(self):
#         return "im similar to a duck!"
    
# def makeSound(duck):
#     print(duck.sound())

# #creating instances
# duck= Duck()
# anotherBird= Anotherbird()
# #calling methods
# makeSound(duck)
# makeSound(anotherBird)

# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def draw(self):
#         "Abstract method" #class or method ko rule/blueprint define 
#         return
# class circle(shape):
#     def draw(self):
#         super().draw()
#         print("Draw a circle")
#         return
# class rectangel(shape):
#     def draw(self):
#         super().draw()
#         print("Draw a rectangle")
#         return
# shapes = [circle(), rectangel()]
# for shp in shapes:
#     shp.draw()

#method overloading
# def add(*nums):
#     return sum(nums)
# result1 = add(10, 25)
# result2 = add(10, 25, 35, 40, 30, 50)

# print(result1)
# print(result2)



        
            
