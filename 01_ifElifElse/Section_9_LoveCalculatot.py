# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name = name1.lower() + name2.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")

calculate = (t + r + u + e)*10 + (l + o + v + e)

if (calculate <10) or (calculate >= 90):
    print(f"Your score is {calculate}. You go together like coke and mentos.")
elif (calculate >= 40) and (calculate < 50):
     print(f"Your score is {calculate}. You are alright together.")
else:
    print(f"Your score is {calculate}.")
    