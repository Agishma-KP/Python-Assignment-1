# Exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
num = 23
textnum = "57"
decimal = 98.3
print("Type of num:", type(num))
print("Type of textnum:", type(textnum))
print("Type of decimal:", type(decimal))
sum_of_vars = num + int(textnum) + decimal
print("Sum of variables:", sum_of_vars)
print("Type of sum:", type(sum_of_vars))

# Exercise 8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes = days_in_year * hours_in_day * minutes_in_hour
print("This program calculates the total number of minutes in a year.")
print(f"Total minutes in a year: {total_minutes}")

# Exercise 9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")


