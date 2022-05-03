import random
min = 1
max = int(input("Numbers of sides of the dice?\n"))
again = "yes"
while again == "yes" or again == "y" or again == "S" or again == "sim" or again == "SIM" or again == "s" or again == "YES":
    print("Rolling the dice...")
    print("The result is: {}".format(random.randint(min, max)))
    again = str(input("Roll again?\n"))
print("End of execution!")