input_number = int(input("Choose a number"))

while input_number > 0:
    if (input_number % 2) == 0:
        input_number / 2
        print(input_number)
    else:
        input_number * 3 + 1
        print(input_number)
