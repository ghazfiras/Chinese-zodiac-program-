while True:
    birth_year = int(input("Enter your birth year: "))
    i = birth_year % 12
    if i == 0:
        print("Your Chinese zodiac sign is: Monkey")
    elif i == 1:
        print("Your Chinese zodiac sign is: Rooster")
    elif i == 2:
        print("Your Chinese zodiac sign is: Dog")
    elif i == 3:
        print("Your Chinese zodiac sign is: Pig")
    elif i == 4:
        print("Your Chinese zodiac sign is: Rat")
    elif i == 5:
        print("Your Chinese zodiac sign is: Ox")
    elif i == 6:
        print("Your Chinese zodiac sign is: Tiger")
    elif i == 7:
        print("Your Chinese zodiac sign is: Rabbit")
    elif i == 8:
        print("Your Chinese zodiac sign is: Dragon")
    elif i == 9:
        print("Your Chinese zodiac sign is: Snake")
    elif i == 10:
        print("Your Chinese zodiac sign is: Horse")
    elif i == 11:
        print("Your Chinese zodiac sign is: Sheep")

#more efficient way to do it:

#zodiac_signs = {
#    0: "Monkey",
#    1: "Rooster",
#    2: "Dog",
#    3: "Pig",
#    4: "Rat",
#    5: "Ox",
#    6: "Tiger",
#    7: "Rabbit",
#    8: "Dragon",
#    9: "Snake",
#    10: "Horse",
#    11: "Sheep"
#}
#print(f"Your Chinese zodiac sign is: {zodiac_signs[i]}")