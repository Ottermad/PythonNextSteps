# My Fortune Cookie

import random

# put answers in a list

answers = [
    "A beautiful, smart, and loving person will be coming into your life.",
    "A dubious friend may be an enemy in camouflage.",
    "A feather in the hand is better than a bird in the air.",
    "A fresh start will put you on your way.",
    "A friend asks only for your time not your money.",
    "A friend is a present you give yourself.",
    "A gambler not only will lose what he has, but also will lose what he doesn’t have."
]

print("Welcome to My Fortune Cookie.")

# get the user's question
question = input("Press ENTER to get a fortune.\n")

print("seeing into the future ...\n" * 4)

# use the randint function to select the correct answer
choice = random.randint(0,7)

# print the answer to the screen
print(answers[choice])

# exit nicely
input("\n\nPress the RETURN key to finish.")
