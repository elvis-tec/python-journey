number = 2  # integer
decimal_number = 2.5  # float
complex_number = 2 + 3j  # complex -> real + imaginary -> 2 + 3i

print(number)
print(decimal_number)
print(complex_number)

print(1 + 2)  # sum
print(1 - 2)  # difference
print(1 * 2)  # product
print(1 / 2)  # division
print(1 % 2)  # modulo -> returns the remainder of the division
print(1 ** 2)  # exponentiation -> 1 to the power of 2
print(1 // 2)  # floor division -> returns the integer part of the division

# overwrite the value of number with the sum of 10 and the current value of number
number = 10 + number
print(number)

number += 10  # shorthand for number = number + 10
print(number)

number -= 10  # shorthand for number = number - 10
print(number)

number *= 10  # shorthand for number = number * 10
print(number)

number /= 10  # shorthand for number = number / 10
print(number)

number %= 10  # shorthand for number = number % 10
print(number)

number **= 10  # shorthand for number = number ** 10
print(number)

number //= 10  # shorthand for number = number // 10
print(number)
