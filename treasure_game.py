print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
direction=input("You are at a cross road. Where do you want to go?\n")

if direction=="left":
    cross_the_lake=input('''You've come to a lake. There is an island in the middle of the lake.\n
  Type "wait" to wait for a boat. Type "swim" to swim across.\n''')

    if cross_the_lake=="wait":
        door=input('''You arrive at the island unharmed. There is a house with 3 doors.
  One red, one yellow and one blue. Which colour do you choose?\n''')

        if door=="yellow":
            print("You found the treasure. YOU WIN!!!!")
        elif door=="red":
            print("It's a room full of fire.\n GAME OVER!!!!")
        elif door=="blue":
            print("You enter a room of beasts.\n GAME OVER!!!!!")
        else:
            print("GAME OVER!!!!!")


    else:
        print("you get attacked by an angry trout.\n GAME OVER!!!!!!!")


else:
    print("You fall into a hole,\n GAME OVER!!!!")