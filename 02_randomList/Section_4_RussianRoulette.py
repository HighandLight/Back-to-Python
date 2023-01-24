# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 

result = random.choice(names)
print(result)

#2
num_items = len(names)

random = random.randint(0, num_items -1)
result2 = names[random]
print(result2)