from tkinter import *

# okno
window = Tk()
window.title("Pevod měn")
window.minsize(500, 500)
window.resizable(False, False)

# Label
label_1 = Label(text="Nový Label 1", font=("Helvetica", 20, "bold"))
label_1.pack()


# Tlačítko
def change_text():
    #                  Tou 1.0 mu říkám začni prvním řádkem
    label_1["text"] = text_field.get("1.0", END)


button_1 = Button(text="Klikni na mě", command=change_text, font=("Helvetica", 20, "bold"))
button_1.pack(pady=(150, 50))

# Textové pole
text_field = Text(width=40, height=10)
text_field.focus()
text_field.pack()
# text_field.get("1.0", END)

# Hlavní cyklus
window.mainloop()
