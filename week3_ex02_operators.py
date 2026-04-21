# question 1 : arithmetic and assignment operators
X = 7
Y = 10
X += 3
Y -= 2
result = X / Y
print (result)
#-----------------------------------------------------------------------------
# Question 2 : comparison AND LOGICAL OPERATORS
a = 10
b = 20
c = 30
a_greater_than_b = a > b
b_is_even = b % 2 == 0
c_less_than_a = c < a
final_condition = a_greater_than_b and b_is_even and c_less_than_a
print (final_condition)

#-----------------------------------------------------------------------------
# Question 3 : conditional statements
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade: A") 
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:    print("Grade: F")
print("your grade is:" , Grade)

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals
 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
 
operation = input("Enter an operation (+, -, *, /): ")
 
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation"
 
print("Result:", result)

