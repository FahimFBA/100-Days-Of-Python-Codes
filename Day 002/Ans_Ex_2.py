# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Years = 90 - int(age)

Months = round(Years * 12)

Weeks = round(Years * 52)

Days = round(Years * 365)

print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")