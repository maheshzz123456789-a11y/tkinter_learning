from tkinter import *

window = Tk()
window.minsize(300, 300)
window.config(padx=100, pady=200)
window.title("my first GUI program")

my_label = Label(text="new text", font=("Arial", 15))
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text=" don't Click here")
new_button.grid(column=3, row=0)


input = Entry()
input.grid(column=4, row=3)
input.get()


window.mainloop()