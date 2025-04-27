from customtkinter import *

window = CTk()
window.geometry("1000x2000")
window.title("logika")
window.configure(fg_color="yellow")

knopka = CTkButton(window, text="Клікни")
knopka.pack()

nadpus = CTkLabel(window, text="Текст")
nadpus.pack()

window.mainloop()