num_char = len(input("What is your name?\n"))
print(num_char)

# print("Your name contains " + num_char + " characters") It will provide an error message: TypeError: can only concatenate str (not "int") to str

# We need to change the int to string first

new_num_char = str(num_char) # converting the num_char from int to string and assigning the value to a new variable named new_num_char

# It is called type casting / type conversion

print("Your name contains " + new_num_char + " characters")

a = float(123)
print(type(a)) # we use type to get the type of the value / variable

print(70 + float("100.5"))