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

#REVISION
#membership and identity operator
# app="i have an apple"
# print("a" in app)

# app="i have an apple"
# print("a"not in app)

# app="i have an apple"
# print("k" not in app)
#membership operator in set
# var={10,20,30,40,50}
# a=10
# b=20
# print(b, "in", var, ":", b in var)
# var={(10, 20),30,40,50}
# a=10
# b=20
# print ((a,b),"in", var, ":",(a,b))

# #membershp in dictonries
# var={1:20, 2:20, 3:30} #it checks only key and not values
# a=2
# b=20
# print(a, "in", var, ":", a in var)
# print(b, "in", var, ":", b in var)

#IDENTITY OPERATOR
# a= [1, 2, 3, 4, 5]
# print("id(a) :", id(a))
# b=[1,2,3,4,5]
# c=a
# print(a is c)
# print(a is b)
# print("id(b):", id(b))
# print("id(c)", id(c))
#IS NOT
# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# c=a
# print(a is not c)
# print(a is not b)

# print("id(a):", id(a))
# print("id(b):", id(b))
# print("id(c):",id(c))
#BITWISE OPERATOR

# a=60 #AND operator
# b=13
# print("a:",a, "b:",b, "a&b:",a&b)
# print("a:",bin(a))
# print("b:", bin(b))
# a=60 #OR OPERATOR
# b=13
# c=a|b
# print(bin(c))
# a=60 #XOR operator
# b=13
# c=a^b
# print(bin(c))
# a=60 #NOT operator
# b=~a
# print(bin(b))
#bitwise rightshitft 
# a=60
# c=a>>2
# print(bin(c))
# #bitwise leftshit
# a=60
# c=a<<2
# print(bin(c))
# #IF-ELSE STATEMENT
# age=5
# print("age:",age)
# if age>=8:
#     print("is eligible to vote")
# else:
#     print("not eligible to vote")
#NESTED IF STATEMENT
# num=88
# if num%2==0:
#     if num%3==0:
#            print("divisible by 2 and 3")
# print("...execution stops...")

 











        
            
