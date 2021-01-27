print("-----------------T  I  P     C  A  L  C  U  L  A  T  O  R--------------------")
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill (in $)? \n"))
people = float(input("How many people are there to split the bill equally? \n"))
percentage = float(input("What percentage tip would you like to give? (Choose from here: 10, 12 or 15 )\n"))
if (percentage == 10):
    print("Each person should pay (with Tip): " , (((total_bill*0.1)+total_bill)/people))
elif (percentage == 12):
    print("Each person should pay (with Tip): " , (((total_bill*0.12)+total_bill)/people))
elif (percentage == 15):
    print("Each person should pay (with Tip): " , (((total_bill*0.15)+total_bill)/people))
