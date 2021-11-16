import math
input_number = int(input("Choose a number: "))


if input_number % 2 == 0:
    new_number = int(math.floor(input_number / 2))
    print(new_number)
else:
    new_number = int(math.floor(input_number * 3 + 1))
    input_number * 3 + 1
    print(new_number)
