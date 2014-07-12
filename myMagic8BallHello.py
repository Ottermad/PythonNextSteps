# My Magic 8 Ball

import random

# put answers in a tuple

answers = (
    "Go for it"
    "No way, Jose!"
    "I'm not sure. Ask me again."
    "Fear of the unkown is what imprisons us."
    "It would be madness to do that."
    "Only you can save mankind!"
    "Makes no difference to me, do or don't - whatever"
    "Yes, I think on balance that is the right choice"
)

print("Welcome to MyMagic8Ball.")
name = input("What is your name?")

# get the user's question
question = input("Ask me for advice, " + name + " then press ENTER to shake me.\n")

print("shaking ...\n" * 4)

# use the randint function to select the correct answer
choice = random.randint(0,7)

# print the answer to the screen
print(answers[choice])

# exit nicely
input("\n\nThanks for playing, " + name + ". Press the RETURN key to finish.")
