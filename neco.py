#1 = kamen
#2 = nuzky
#3 = papir

import random

class hra:
    def roll(self):
        firstPlayer = random.randint(1, 3)
        secondPlayer = random.randint(1, 3)
        if firstPlayer == 1 and secondPlayer == 1:
            print("Draw")
        elif firstPlayer == 1 and secondPlayer == 2:
            print("First player won")
        elif firstPlayer == 1 and secondPlayer == 3:
            print("First player lost")
        elif firstPlayer == 2 and secondPlayer == 1:
            print("First player lost")
        elif firstPlayer == 2 and secondPlayer == 2:
            print("Draw")
        elif firstPlayer == 2 and secondPlayer == 3:
            print("First player won")
        elif firstPlayer == 3 and secondPlayer == 1:
            print("First player won")
        elif firstPlayer == 3 and secondPlayer == 2:
            print("First player lost")
        elif firstPlayer == 3 and secondPlayer == 3:
            print("Draw")
        return firstPlayer, secondPlayer


dice = hra()
print(dice.roll())