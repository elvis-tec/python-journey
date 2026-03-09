n1 = input("Enter a number: \n")
n2 = input("Enter another number: \n")

n1 = int(n1)
n2 = int(n2)

plus = n1 + n2
minus = n1 - n2
multiply = n1 * n2
divide = n1 / n2

msj = f"""
The result of the operation is:
Plus: {plus}.
Minus: {minus}.
Multiply: {multiply}.
Divide: {divide}.
"""

print(msj)
