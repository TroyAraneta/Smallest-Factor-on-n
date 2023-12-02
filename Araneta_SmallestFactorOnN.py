integer = int(input("Enter an integer >= 2: "))
if integer <= 2:
    print("Invalid input. Enter a number greater than 2.")
else:
    for num in range(2, integer):
        factor = integer % num
        if factor == 0:
            print(f"The smallest factor other than 1 for {integer} is {num}")
            break
    else:
        print(f"{integer} is a prime number")
