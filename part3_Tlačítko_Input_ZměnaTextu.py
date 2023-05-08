from tkinter import *

# okno
window = Tk()
window.title("Pevod měn")
window.minsize(500, 500)
window.resizable(False, False)

# Label
label_1 = Label(text="Nový Label 1", font=("Helvetica", 20, "bold"))
label_1.pack()

# Způsob měnit text 2 varianty
# label_1["text"] = "Další text"
# label_1.config(text="Toto je zcela nový text")


# Tlačítko
def change_text():
    # vezme napsanou hodnotu v moment co uživatel klikne na tlačítko
    label_1["text"] = input_1.get()

    # Vymaže input (to pole vyčistí od 0 písmena až po konec)
    input_1.delete(0, END)


#                       velký pozor zde u funkce se ty závorky nepíšou v commandu(voláme funkci)!!!!!
button_1 = Button(text="Klikni na mě", command=change_text, font=("Helvetica", 20, "bold"))
button_1.pack(pady=(150, 150))

# Input (vstup, to pole kam se zadává text)
input_1 = Entry(width=30, font=("Helvetica", 20))

# Vyplní políčko od 0
input_1.insert(0, string="Max")

# Dá text za slovo Max, jde dát podle čísla i třeba po 2 písmenku
input_1.insert(END, string="WORLD")

# Automaticky hned je kliknuto do pole kam se dává text a může se psát
input_1.focus()
input_1.pack()

# Hlavní cyklus
window.mainloop()
