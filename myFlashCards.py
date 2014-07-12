# myGlossary.py

from tkinter import *

# key press functions:
def getAnswer():
    entered_text = entry.get()
    output.delete(0.0, END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)

def getQuestion():
    question.delete(0.0, END)
    try:
        definition = random.choice(keys)
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)

##### main:
window = Tk()
window.title("My Coding Club Glossary")

# Add a submit button:
Button(window, text="GET QUESTION", command=click).grid(row=0, column=0, sticky=W)

# Add a submit button:
Button(window, text="GET ANSWER", command=getAnswer).grid(row=0, column=0, sticky=E)

# create text entry box
question = Text(window, height=1, width=20 wrap=WORD, background="light green")
question.grid(row=1, column=0, sticky=W)

# create another label
Label(window, text="\nDefinition:").grid(row=3, column=0, sticky=W)

# create text box
output = Text(window, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=1, sticky=W)

# The dictionary:
my_glossary = {
    "algorithm": "Step by step instructions to perform a task that a computer could understand.",
    "bug": "A piece of code that is causing a program to fail to run properly or at all.",
    "binary number": "A number represented in base 2."
    }

keys = []

for key in my_glossary:
    keys.append()

##### Run mainloop
window.mainloop()
