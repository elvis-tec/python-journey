first_name = "Elvis"
last_name = 'Salazar'  # accepts single or double quotes
description = """
This is a string
With multiple lines
and very long text
"""  # triple quotes are used for multi-line strings and docstrings

print(first_name, last_name, description)
print(len(description))  # len() returns the length of the string
print(first_name[0])  # indexing
print(first_name[0:2])  # slicing from index 0 to 2
print(first_name[2:])  # slicing from index 2 to the end
print(first_name[:2])  # slicing from the start to index 2
print(first_name[:])  # slicing from the start to the end
