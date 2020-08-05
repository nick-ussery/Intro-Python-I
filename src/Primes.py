import math
num = int(input("Put in number to see if it is Prime: "))

for i in range(2, math.floor(math.sqrt(num))):
    if (num % i) == 0:
        print(i, "times", num//i, "is", num)
        break
    else:
        print(num, " is a prime number")
