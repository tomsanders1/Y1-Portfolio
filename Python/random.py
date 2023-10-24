import random
number = random.randint(1,10)
print (number)
counter = 1
answer = int(input("guess number: "))
while answer != number:
    if answer < number:
        print ("Higher")
    elif answer > number:
        print ("Lower")
    answer = int(input("Wrong, try again: "))
    counter = counter + 1

print ("Well done! You took", counter,"attempts.")