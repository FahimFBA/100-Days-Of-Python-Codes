print("Welcome to the rollercoaster")
height = int(input("What is your height? (in CM): "))

# if-else

if height >= 120:
    print("Congratulations! You can ride the rollercoaster!")

    age = int(input("What is your age? "))

    # Nested if-else statements

    if age <= 10:
        print("You need to pay $5 for the ticket.")
    elif age <= 18:
        print("You need to pay $7 for the ticket.")
    else:
        print("You need to pay $12 for the ticket.")

else:
    print("We are sorry. You have to grow taller before you can ride here.")
