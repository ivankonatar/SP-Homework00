
'''
Task 2. Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def Task2():

    n=eval(input("unesite cijeli broj n: "))

    if not isinstance(n,int):
        print("broj nije cijeli!")
        quit()
    if not n>0:
        print("broj nije pozitivan!")
        quit()

    suma=0
    for i in range(0,n):
        suma+=i**2

    return suma

print(Task2())
