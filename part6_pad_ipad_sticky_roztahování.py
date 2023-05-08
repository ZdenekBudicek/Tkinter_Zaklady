from tkinter import *

# Okno
window = Tk()
window.title("Seznam úkolů")
window.minsize(400, 400)
window.iconbitmap("icons/icon_pen.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#72be34"
button_color = "#ff9122"
window.config(bg=main_color)

# Framy
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - obsah
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color)
user_input.grid(row=0, column=0, pady=5)
# pad je vnější okraj a ipad je vnitřní okraj
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=15)

# Text frame - obsah
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font)
list_box.grid(row=0, column=0)

# Button frame - obsah
remove_button = Button(button_frame, text="Odstranit položku", borderwidth=2, font=main_font, bg=button_color)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_color)
save_button = Button(button_frame, text="Uložit položku", borderwidth=2, font=main_font, bg=button_color)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_color, command=window.destroy)
remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)

# Výková zóna
# north, south, east, west
# Sticky šoupe položkou v daném sloupci row, column
# Lze to i kombinovat že se roztáhne od západu na východ například
test_label = Label(button_frame, text="testik", bg="red", fg="white")
test_label.grid(row=1, column=0, sticky=W+E)

# Hlavní cyklus
window.mainloop()
