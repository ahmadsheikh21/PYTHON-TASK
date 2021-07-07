# Program to check wether donor and recepient blood tye is compatible or not.
# Conditions for compatibility are:
# If a recipient is Rh-negative, the donor must also be Rh-negative.
# If a recipient is Rh-positive, the donor can be either Rh-positive or Rh-negative.

# Initialising counters
success = 0
count = 0
per = 0.0

# function to check if blood type is compatible or not
def isCompatible(donor, recepient):
    if recepient == '+':
        return 1
    elif recepient == '-' and donor =='-':
        return 1
    else:
        return 0

# using recursion to validate user inputs
while True:

    # check against each input to check input validity
    # for a successful run conditions have to be false
    print("Donor's blood group")
    abogroupD = input("ABO Type: ")
    if abogroupD not in ('A', 'B', 'AB', 'O'):
        print("Retry! invaild blood group.")
        continue
    rhtypeD = input("Rh Type:")
    if rhtypeD not in ('+', '-'):
        print("Retry! invalid blood type.")
        continue
    print("Recepient's blood group")
    abogroupR = input("ABO Type: ")
    if abogroupR not in ('A', 'B', 'AB', 'O'):
        print("Retry! invaild blood group.")
        continue
    rhtypeR = input("Rh Type:")
    if rhtypeR not in ('+', '-'):
        print("Retry! invalid blood type.")
        continue

    # incrementing counters
    success += isCompatible(rhtypeD, rhtypeR)
    count += 1

    # check if user wants to compare another blood type or exit
    check = input("Do you want another check(y/n)? ")
    if check=='n':
        break

# display results
per=(success/count) * 100
print("Total num of inputs: ", count)
print("Compatible results: ", per)
print("Thank you.")