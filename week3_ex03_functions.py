# Question 1: Basic Function Definition and Calling

def greet():
    print("Hello, World!")

greet()


#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

def personalized_greeting(name):
    print(f"Hello, {name}!")

personalized_greeting("Sabah")


#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

def square(number):
    return number ** 2

print(square(5))


#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

def rectangle_area(length, width):
    return length * width

print(rectangle_area(4, 5))


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

def apply_operation(func, number):
    return func(number)

def double(number):
    return number * 2

print(apply_operation(double, 7))   # double(7) → 14
print(apply_operation(square, 3))   # square(3) → 9