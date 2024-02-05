# This is a Prime Determiner Script in Python
# This imports math function
import math
while True:
    number = int(input("Enter a Number: "))
    flag = False
    for x in range(2, math.floor(math.sqrt(number) + 1)):
        if number % x == 0:
            flag = True
            break
    if flag:
        print(number, "is a composite number.")
    else:
        print(number, "is a prime number.")
    connect = input("Do you want to continue?(y/n): ")
    if connect.lower() == "n":
        break


