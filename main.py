# class Grandparent:
#     def about(self):
#         print('I am Grandparent')
#     def about_myself(self):
#         print('I am Grandparent')
#
# class Parent(Grandparent):
#     def about_myself(self):
#         print('I am Parent')
#
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
#
# vasya = Child()

class Computer:
    def calculator(self):
        print('Calculating...')

class Display:
    def display(self):
        print('I display the image on the screen')
class Smartphone(Display, Computer):
    pass

iphone = Smartphone()

iphone.calculator()
iphone.display()