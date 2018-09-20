
'''
Task 5. Give a single line command that computes the sum from Task 4,
relying on Python's comprehension syntax and the built-in sum function.
'''

print(sum(i**2 for i in range(1,6) if i%2!=0))