print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You cna ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("pleas pay $7.")
    else:
        print("please pay $12.")
else: 
    print("Sorry, You have to grow taller before you can ride.")
    