'''
import random

class xyz:
    float_number=1.0

    def random_function():
        return random.randrange(1,100)

xyz1=xyz
print(xyz1.float_number)
print(xyz1.random_function())

'''

'''
class calculator:
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b 
    def division(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("zero division error")


calc=calculator
print('enter two number⬇️') 
print('_'*30)
first=int(input('enter first number: '))
second=int(input('enter second number: '))
print('_'*30)

while True:
    choice=input('enter your choice:\n1.[+]\n2.[-]\n3.[*]\n4.[/]\n')
    print('_'*30)
    match choice:
        case '+':
            print(calc.addition(first,second))
        case '-':
            print(calc.subtraction(first,second))
        case '*':
            print(calc.multiplication(first,second))
        case '/':
            print(calc.division(first,second))
        case _:
            print('HEY, choose valid choice:')

    ch=input('do you want to continue? [y/n]: ')
    if ch.lower()=='n':
        break
'''
