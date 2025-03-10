# y="bidhi"
# def my_function():
#     y = str(10)
#     print (y)
#     print(type(y))
# my_function()
# print(y)
# print(type(y))
# my_List =[1, 2, 3]
# my_List.append(4)
# my_list =[1,2,3]
# del my_list[1]

# x=10
# x %= 3
# print(x)

# has_passport = False
# has_visa = True

# if has_passport or has_visa:
#     print ("can travel abroad")

# if has_passport and has_visa:
#     print ("can travel abroad********************")
# else:
#     print("can't travel")

# has_passport = False
# has_visa = False


# age=25
# income=50000
 
# if age>18 and income > 30000:
#     print("eligible for loan")
# a=60
# b=13
# print ("a:",a, "b:",b, "a&b:",a&b)

# print ("a:", bin(a))
# print ("b:", bin(b))

# def greet(name):
#     return f"hello, {name}!"
# print (greet(("haha")))

# def add_number(a,b):
#     return a+b

# result = add_number(5, 10)
# print(result)

# square = lambda a: a * a
# print(square(4))

# def factorial(n):
#     if n == 1:
#         return 1
#     print(factorial(n-1),"=====================================")
#     return n*factorial(n-1)
# print (factorial(5))

# fruits= ["apple", "banana", "cherry"]
# print ("banana"in fruits)

# text= "hello, world!"
# print("z" not in text)

# print ("ell" in "hello")



# def myfunc():
#     global x
#     x=200
    
# myfunc()
# print(x)

# def myfunc1():
#     x="jane"
#     def myfunc2():
#         nonlocal x
#         x="hello"  (overriding global variable)
#         print(x,"&&&&&&&&&&&&&&&&&&&&&&&&&")

#     myfunc2()
#     return x
# print(myfunc1())

# def myfunc1():
#     x="jane"
#     def myfunc2():
#         x="hello"
#         print(x)

#     myfunc2()
#     return x
# print(myfunc1())

# a="hello, world!"
# print (a[1])  

# for x in "banana":
#     print(x)

# a = "hello, world"
# print(len(a))

# b="hello, world"
# print(b[-5:-2])

# x="welcome"
# print(x[3:5])

# a=0b1010
# b=0b1100
# c=a&b #bitwise and
# print (bin(c))

# a=0b1010
# b=0b1100
# c=a|b #bitwise or
# print(bin(c))

# a= 0b1010
# b= 0b1100 bitwise XOR
# c=print(bin(c))

# a= 10
# b=4
# c=~a
# print("~a",~a)

# age=36
# txt=f"my name is john, i am {age}"
# print(txt)

# txt="we are the so-called "vikings" from the north"
# print(txt)

# txt="we are the so-called \"vikings\" from the north"
# print(txt)

# thislist=["apple", "banana", "cherry", "orange","kiwi","melon", "mango"]
# print(thislist[-4:-1])

# thislist=["apple", "banana", "cherry", "orange","kiwi","melon", "mango"]
# (thislist[1:3])=["blackcurrant","watermelon"]
# print(thislist)

# thislist=["apple", "banana", "cherry"]
# (thislist[1:3])=["blackcurrant","watermelon"]
# print(thislist)

# thislist=["apple", "banana", "cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist=["apple", "banana", "cherry"]
# thislist.append("watermelon")
# print(thislist)

# thislist=["apple", "banana", "cherry"]
# thistuple=("kiwi","orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist=["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist=list=["apple", "banana", "cherry"]
# i=0
# while i < len(thislist):
#     print(thislist[i])
#     i=i+1

# thislist=["apple","banana","cherry"]
# [print(x) for x in thislist]

# fruits=["apple","banana","cherry", "kiwi","mango"]
# newlist=[]

# for x in fruits:
#     if "a" in x:    {check a}
#         newlist.append(x)

# print(newlist)

# class car:
#     def __init__(self, color, model):
#       self.color = color
#       self.model = model
# def honk(self):
#     print("beep beep!")

# my_car = car("red", "toyota")
# my_car.honk()
  
# class bankAccount:
#     def __init__(self, balance):
#         self.__balance = balance #privaate attribute
#     def deposit(self, amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance

# account = bankAccount(100)
# account.deposit(50)
# print(account.get_balance())

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
    
# }
# x= thisdict["model"]
# print(x)
# x= thisdict.get("model")
# print(x)
# x= thisdict.keys()
# print(x)
# x= thisdict.values()
# print(x)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964    
# }
# if "model" in thisdict:
#     print("yes,'model' is one of the keys in the thisdict dictonary")
# else:
#     print("no")

# for x in thisdict.items():
#     print(x)


# x=thisdict.values()
# print(x)

# thisdict["estd"]="2020"
# print (x)

# x=thisdict.items() #to see what changes have been made, it gives values in tuple.
# print(x)

# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))

# x={'type': 'fruit', 'name': 'apple'}
# for y in x:
#     print(y)
# for y in x.values():
#     print(y)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print ("Drive!")
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print ("Sail!")
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print ("Fly!")

# car1= Car("ford", "mustang")
# boat1=Boat("Ibiza", "Touring 20")
# plane1=Plane("boeing", "747")

# for x in (car1, boat1, plane1):
#     x.move() #only calling one time 

#DICTONARY

# thisdict= {
#     "brand":"ford",
#     "model":"mustang",
#     "year":1968
# }
# print(thisdict)

# thisdict= {
#     "brand":"ford",
#     "model":"mustang",
#     "year":1968
# }
# print(thisdict["brand"]) #can be reffered to by using same the key name

# thisdict= {
#     "brand":"ford",
#     "model":"mustang",
#     "year":1968,
#     "year":2020  #will override, cannot have duplicate values
# }
# print(len(thisdict)) #number of items in dict

# thisdict= {
#     "brand":"ford",
#     "model":"mustang",
#     "year":1968
# }
# print(type(thisdict)) #data type of dict

# thisdict= dict(name="john", age="18", country="norway") #using the dict() func
# print(thisdict) 

# car= {
#     "model":"mustang",
#     "brand":"ford"    
# }
# print(car.get("model")) #get method to print the value of the "model" key of the car dictionary.

#INHERITANCE

# class parent: #parent class
#     def parentMethod(self):
#         print("calling parent method")
# #child class
# class Child(parent):
#     def childMethod(self):
#         print("calling child method")

# c= Child()
# c.childMethod()#calling method of child class
# c.parentMethod()


# #multiple inheritance
# class division:
#     def __init__(self, a, b):
#         self.n=a
#         self.d=b
#     def divide(self):
#         return self.n/self.d
# class modulus:
#     def __init__(self, a, b):
#          self.n=a
#          self.d=b
#     def divide(self):
#         return self.n%self.d
    
# class div_mod(division, modulus):
#     def __init__(self, a, b):
#         self.n=a
#         self.d=b
#     def div_and_mod(self):
#         divval=division.divide(self)
#         modval=modulus.mod_divide(self)
#         return (divval, modval)
# x=div_mod(10,3)
# print("division:", x.divide())
# print("mod_division:", x.mod_divide())
# print("divmod:", x.div_and_mod())

#multi inheritance

#hybrid inheritance
# class CEO:
#     def ceoMethod(self):
#         print("i am the CEO")
# class Manager(CEO):
#     def managerMethod(self):
#         print("i am Employee one")
# class Employee1(Manager):
#     def employee1Method(self):
#         print ("i am EMployee one")
# class Employee2(Manager, CEO):
#     def employee2(self):
#         print("i am employee two")
# emp= Employee2()
# emp.managerMethod()
# emp.ceoMethod()
# emp.employee2Method()

#super function 
#parent class:
# class ParentDemo:
#     def __init__(self, msg):
#         self.message=msg
#     def showMessage(self):
#         print(self.message)
# #child class
# class ChildDemo(ParentDemo):
#     def __init__(self, msg):
#         #use of super function
#         super().__init__(msg)
    
#     #creating instances
# obj= ChildDemo("Welcome to Tutorialspoint!")
# obj.showMessage()

# from abc import ABC, abstractmethod
# class demo (ABC):
#     @abstractmethod
#     def method1(slef):
#         pass
        
#     def method2(self):
#         print("concrete method")

# class concreteclass():
#     def method1(self):
#         print("abstract method")
#         return
    
# obj=concreteclass()
# obj.method1()

# #DECORATOR
# def make_pretty(func):
#     #define the inner function
#     def inner():
#         print("line 2")
#         #add some assitional behavior to decorated function
#         print("i got decorated")
#         #call original funtion
#         func()
#         print("line 3")
#     #return the inner funtion 
#     return inner 
# #define ordinary funtion 
# @make_pretty
# def ordinary():
#     print("line 3")
#     print("i am ordinary")

# ordinary()

# # decorated_func= make_pretty(ordinary)
# # decorated_func()







                

















    















