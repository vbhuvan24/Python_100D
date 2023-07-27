#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random

coins = random.randint(0, 1)

if coins == 1:
    print("Heads")
else:
    print("Tails")