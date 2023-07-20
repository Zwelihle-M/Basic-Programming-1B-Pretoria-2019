from tkinter import *
import random

root = Tk()
root.resizable(False, False)

root.title('Coinflipper')

topframe = Frame(root)
topframe.pack()
botframe = Frame(root)
botframe.pack(side=BOTTOM)
midframe = Frame(root)
midframe.pack()

choice = Label(topframe, text="Enter the number of flips: ")
choice.grid(row=1)
ent = Entry(topframe)
ent.grid(row=1, column=2)

clickit = Button(botframe, text="Flip coin!")
clickit.pack()

out = Text(midframe, width=15, height=1)
out2 = Text(midframe, width=15, height=1)
out.grid(row=1, column=1, columnspan=3)
out2.grid(row=2, column=1, columnspan=3)


def flipy(event):
    guess = ent.get()
    heads = []
    tails = []

    if guess == '' or guess == str(guess):
        out.delete(1.0, "end-1c")
        out.insert("end-1c", 'Invalid')

    for flips in range(int(guess)):
        out.delete(1.0, "end-1c")
        out2.delete(1.0, "end-1c")
        random_number = random.randint(1, 2)
        if random_number == 1:
            heads.append("Heads")
        elif random_number == 2:
            tails.append("Tails")

    out.insert("end-1c", len(tails))
    out.insert("end-1c", " -TAILS")
    out2.insert("end-1c", len(heads))
    out2.insert("end-1c", " -HEADS")


clickit.bind("<Button-1>", flipy)

root.mainloop()
