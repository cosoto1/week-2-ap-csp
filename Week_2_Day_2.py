# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Caiden"
age = 17
favorite_color = "Red"
favorite_number = 3

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print(f"Hi, my name is {first_name} and my favorite color is {favorite_color}")

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number
print(f"My favorite number plus 10 is: {favorite_number + 10}")
print(f"My favorite number times 2 is: {favorite_number * 2}")
print(f"My favorite number squared is: {favorite_number ** 2}")
print(f"My favorite number divided by 2 is: {favorite_number / 2}")


#  Step 4: User Input Practice
# Ask the user two questions and combine answers
hobby = input("What’s one of your favorite hobbies? ")
food = input("What’s your favorite food? ")
print(f"Cool! You like {hobby} and enjoy eating {food}!")



# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
future_age = age + favorite_number
print(f"In {favorite_number} years, {first_name} will be {future_age} years old, still loving the color {favorite_color}!")