flat_number = int (input("Please, enter your flat number: "))


entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print("Your entrance number is: " + str(entrance_number))
print("Your floor number is: " + str(floor_number))