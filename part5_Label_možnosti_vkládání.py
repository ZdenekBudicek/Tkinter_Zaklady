from tkinter import *

# Okno
window = Tk()
window.title("Převod měn")
window.minsize(500, 500)
window.resizable(False, False)

# Label
# Pack = málo variabilní (málo se s textem šoupe)
# grid = zlatá střední cesta (ale chová se hloupě)
# place = hodně specifický

label_1 = Label(text="První label", font=("Helvetica", 20))
# label_1.pack(side="bottom")
# label_1.place(x=0, y=0)
label_1.grid(row=0, column=0)

label_2 = Label(text="Druhý label", font=("Helvetica", 20))
# label_2.pack(side="bottom")
# label_2.place(x=200, y=200)
label_2.grid(row=1, column=1)

label_3 = Label(text="Třetí label", font=("Helvetica", 20))
# label_3.pack(side="bottom")
# label_3.place(x=250, y=450)
label_3.grid(row=2, column=2)

# Hlavní cyklus
window.mainloop()
