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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
cross1 = input(
    "You're at a cross road. Where do you want to go? 'left' or 'right'")

if cross1 == "left":
    cross2 = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat or 'swim' to swim across.\n"
    )
    if cross2 == "wait":
        color = input(
            "You arrive at the island. There is a house with 3 doors. Red, yellow and blue. Wich colour do you choose?\n"
        )
        if color == "red":
            print("Burned by fire.\n Game Over.")
        elif color == "blue":
            print("Eaten by beasts. \n Game Over.")
        elif color == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
      print("Attacked by trout. \n Game Over.")
else:
    print("You fall into a hole. \n GAME OVER")
