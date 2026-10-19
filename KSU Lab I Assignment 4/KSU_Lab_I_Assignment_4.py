burgerSingle = 0
burgerDouble = 0
fries = 0
onionRings = 0
smallCola = 0
mediumCola = 0
largeCola = 0
smallDrOwl = 0
mediumDrOwl = 0
largeDrOwl = 0

totalPrice = 0.0
tipPrice = 0.0
taxPrice = 0.0

# uses to read user input
def input_choice(userInput, min, max):
    if int(userInput) < min or int(userInput) > max:
        print(f"Please enter an option between {min} and {max}\n")
    elif int(userInput) >= min and int(userInput) <= max:
        return userInput

# uses to read and verify user money input
def input_money(userInput):

    global tipPrice
    global totalPrice

    userInput = userInput.replace("$", "").replace("%", "")
    customTip = float(userInput)

    if customTip >= 0:
        tipPrice = customTip
    else:
        customTip = customTip / 100
        newCustomTipPrice = totalPrice * customTip
        newCustomTipPrice = round(newCustomTipPrice, 2)
        tipPrice = newCustomTipPrice

    return tipPrice

def order():
    run = True

    while run:
        print("Choose an option:")
        print("1. Burgers")
        print("2. Sides")
        print("3. Drinks")
        print("4. Check out")
        userVal = input_choice(input("> "), 1, 4)

        if userVal == "1":
            print("")
            burgers()
        if userVal == "2":
            print("")
            sides()
        if userVal == "3":
            print("")
            drinks()
        if userVal == "4":
            print("")
            calculate_tip()
            run = False

def burgers():
    run = True

    global burgerSingle
    global burgerDouble
    global totalPrice

    while run:
        print("1. Big Owl Burger - Single ($5.99)")
        print("2. Big Owl Burger - Double ($7.99)")
        print("3. Return")

        userVal = input_choice(input("> "), 1, 3)

        if userVal == "1":
            burgerSingle += 1
            totalPrice += 5.99
            print("1 Big Owl Burger - Single added\n")
        if userVal == "2":
            burgerDouble += 1
            totalPrice += 7.99
            print("1 Big Owl Burger - Double added\n")
        if userVal == "3":
            print("")
            run = False

def sides():
    run = True
    
    global fries
    global onionRings
    global totalPrice

    while run:
        print("1. Fries ($3.49)")
        print("2. Onion Rings ($2.99)")
        print("3. Get Back")

        userVal = input_choice(input("> "), 1, 3)

        if userVal == "1":
            fries += 1
            totalPrice += 3.49
            print("1 Fries added\n")
        if userVal == "2":
            onionRings += 1
            totalPrice += 2.99
            print("1 Onion Rings added\n")
        if userVal == "3":
            print("")
            run = False

def drinks():
    run = True

    global smallCola
    global mediumCola
    global largeCola
    global smallDrOwl
    global mediumDrOwl
    global largeDrOwl
    global totalPrice

    while run:
        print("1. Small Cola ($1.99)")
        print("2. Medium Cola ($2.49)")
        print("3. Large Cola ($2.99)")
        print("4. Small Dr. Owl ($2.49)")
        print("5. Medium Dr. Owl ($2.99)")
        print("6. Large Dr. Owl ($3.49)")
        print("7. Get Back")

        userVal = input_choice(input("> "), 1, 7)

        if userVal == "1":
            smallCola += 1
            totalPrice += 1.99
            print("1 Scrappy-Cola - Small added\n")
        if userVal == "2":
            mediumCola += 1
            totalPrice += 2.49
            print("1 Scrappy-Cola - Medium added\n")
        if userVal == "3":
            largeCola += 1
            totalPrice += 2.99
            print("1 Scrappy-Cola - Large added\n")
        if userVal == "4":
            smallDrOwl += 1
            totalPrice += 2.49
            print("1 Dr. Owl - Small added\n")
        if userVal == "5":
            mediumDrOwl += 1
            totalPrice += 2.99
            print("1 Dr. Owl - Medium added\n")
        if userVal == "6":
            largeDrOwl += 1
            totalPrice += 3.49
            print("1 Dr. Owl - Large added\n")
        if userVal == "7":
            print("")
            run = False

def calculate_tip():
    run = True

    global totalPrice
    global tipPrice
    global taxPrice

    eighteenPercent = totalPrice * 0.18
    twentyPercent = totalPrice * 0.20
    twentyFivePercent = totalPrice * 0.25

    eighteenPercent = round(eighteenPercent, 2)
    twentyPercent = round(twentyPercent, 2)
    twentyFivePercent = round(twentyFivePercent, 2)

    while run:
        print("Choose a tip option:")
        print(f"1. ${eighteenPercent} (18%)")
        print(f"2. ${twentyPercent} (20%)")
        print(f"3. ${twentyFivePercent} (25%)")
        print("4. Custom")
        print("5. No Tip")

        userVal = input_choice(input("> "), 1, 5)

        if userVal == "1":
            tipPrice = eighteenPercent
            run = False
        if userVal == "2":
            tipPrice = twentyPercent
            run = False
        if userVal == "3":
            tipPrice = twentyFivePercent
            run = False
        if userVal == "4":
            input_money(userVal)
            run = False
        if userVal == "5":
            tipPrice = 0.0
            run = False

    print("")
    taxPrice = calculate_tax()
    print_total()

def calculate_tax():
    taxPrice = totalPrice * 0.06

    return taxPrice

def print_total():
    global totalPrice
    global tipPrice
    global taxPrice

    finalPrice = totalPrice + tipPrice + taxPrice

    totalPrice = round(totalPrice, 2)
    tipPrice = round(tipPrice, 2)
    taxPrice = round(taxPrice, 2)
    finalPrice = round(finalPrice, 2)

    print(f"Subtotal: ${totalPrice}")
    print(f"Tip: ${tipPrice}")
    print(f"Tax: ${taxPrice}")
    print(f"Total: ${finalPrice}")

order()