"""
Task 1. Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the form
of a tuple of length two.
Do not use the built-in functions min or max while implementing your solution.
"""

def minmax():
    x=[]
    n=int(input("unesite duzinu niza: "))

    for i in range(n):
        broj=int(input("Unesite "+str(i+1)+". element niza: "))
        x.append(broj)


    minimalni=x[0]
    maksimalni=x[0]
    for i in range(n):
        if x[i]<minimalni:
            minimalni=x[i]
        if x[i]>maksimalni:
            maksimalni=x[i]

    return minimalni,maksimalni

print(minmax())
