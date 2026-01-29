animal = " elephant Is big "
# upper is a method -> a method is a function that belongs to an object
print(animal.upper())
print(animal.lower())
# its not working because the string has spaces at the beginning
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())  # remove spaces at the beginning
print(animal.rstrip())  # remove spaces at the end
# chaining methods -> capitalize works now because spaces are removed
print(animal.strip().capitalize())
# returns the index of the first occurrence of the substring
print(animal.find("Is"))
print("big" in animal)  # returns True if the substring is in the string
# returns True if the substring is not in the string
print("big" not in animal)
print(animal.replace("ele", "mono"))
