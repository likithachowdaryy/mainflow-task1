
# Variable assignment
x = 10         # Integer
name = "LIKITHA" # String
price = 19.99  # Float
is_active = True # Boolean


# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.0, 20.0)

# Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Set
unique_numbers = {1, 2, 3, 4}

# NoneType
result = None

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")
print(f"Fruits: {fruits}")
print(f"Coordinates: {coordinates}")
print(f"Person Info: {person}")
print(f"Unique Numbers: {unique_numbers}")
print(f"Result: {result}")



#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)




#while loop
count = 0
while count < 5:
    print(count)
    count += 1



def greet(name="World"):
    print(f"Hello, {name}!")

greet()
greet("LIKITHA")


import pandas as pd


# Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Initial list: {fruits}")

# Appending to the list
fruits.append("orange")
print(f"After append: {fruits}")

# Inserting into the list
fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

# Removing from the list using remove()
fruits.remove("banana")
print(f"After remove: {fruits}")

# Removing from the list using pop()
popped_fruit = fruits.pop(2)
print(f"After pop: {fruits}")
print(f"Popped fruit: {popped_fruit}")

# Updating an element in the list
fruits[1] = "kiwi"
print(f"After update: {fruits}")




# Creating a dictionary
person = {"name": "Alice", "age": 25}
print(f"Initial dictionary: {person}")

# Adding elements to the dictionary
person["city"] = "New York"
print(f"After adding city: {person}")

# Modifying an element in the dictionary
person["age"] = 26
print(f"After modifying age: {person}")

# Removing an element using pop()
removed_age = person.pop("age")
print(f"After removing age with pop: {person}")
print(f"Removed age: {removed_age}")

# Removing an element using del
del person["city"]
print(f"After removing city with del: {person}")

# Adding elements back for further demonstration
person["age"] = 26
person["city"] = "New York"

# Removing an element using popitem()
last_item = person.popitem()
print(f"After removing last item with popitem: {person}")
print(f"Last removed item: {last_item}")




# Initial tuple
numbers = (1, 2, 3)
print(f"Initial tuple: {numbers}")

# Adding elements
numbers += (4,)
print(f"After adding an element: {numbers}")

numbers += (5, 6)
print(f"After adding multiple elements: {numbers}")

# Removing elements
numbers_list = list(numbers)
numbers_list.remove(2)
numbers = tuple(numbers_list)
print(f"After removing an element: {numbers}")

# Modifying elements
numbers_list = list(numbers)
numbers_list[0] = 10
numbers = tuple(numbers_list)
print(f"After modifying an element: {numbers}")
