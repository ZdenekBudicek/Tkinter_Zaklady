from tkinter import *

# Okno
window = Tk()
window.minsize(width=500, height=500)
window.resizable(False, False)
window.iconbitmap("icons/icon3.ico")
window.title("Přepočet kurzu")
window.config(bg="black")

# Label                                                                                barva textu
currency = Label(window, text="Eura", font=("Cambria", 20, "bold"), bg="black", fg="white",
                 # rámeček      styl ramečku: flat raised sunken groove  ridge
                 borderwidth=5, relief="groove")
# Odsazení rámečku, nejdou 2 hodnoty jak při pad
currency.pack(ipadx=20)
# Odsazení první 10 od vrchu rámečku k textu a druhé 50 od textu k textu v ose y
# currency.pack(pady=(10, 50))

currency2 = Label(window, text="CZK", font=("Cambria", 20, "bold"), bg="black", fg="white",
                  borderwidth=5, relief="groove")
currency2.pack(ipadx=20)

# Hlavní cyklus
window.mainloop()
