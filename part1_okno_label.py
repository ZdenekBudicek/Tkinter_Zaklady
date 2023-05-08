import tkinter

# tkinter okno
window = tkinter.Tk()
window.title("Moje první okno")
window.minsize(width=800, height=600)
# Může uživatel měnit šířku a výšku
window.resizable(True, True)
# Ikonka co jsem si stáhl
window.iconbitmap("icons/icon.ico")
window.config(bg="#5e8ad6")

window2 = tkinter.Tk()
window2.title("druhé okno")
# hodnoty za + určují kde se okno zobrazí při spuštění
window2.geometry("300x500+1300+400")
window2.resizable(False, False)
window2.iconbitmap("icons/icon2.ico")
window2.config(bg="yellow")

# Label (text)
#                                                     Styl písma , velikost písma,(tučný, kurzívá, podtrhnout atp.)
greet_label = tkinter.Label(window2, text="Hello", bg="white", font=("Helvetica", 24, "bold"))
#                     expand roztáhne ten label do prostřed okna
greet_label.pack(side="top", expand=True)
# Hlavní cyklus
window.mainloop()
