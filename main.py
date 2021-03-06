file = open("pi_dec_1m.txt", "r")
digits = file.read()

while True:
    search = input("Please enter a number to look for in Pi: ")
    try:
        int(search)
    except:
        print("That was not a valid number.")
        continue

    output = digits.find(search)
    if output < 0:
        print("That could not be found in Pi.")
    else:
        print(f"That string was first found at index {output} in Pi.")