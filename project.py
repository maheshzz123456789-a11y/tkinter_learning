from tkinter import *
window = Tk()
window.minsize(300, 300)

window.title("miles to km converter")

my_label = Label(text="Miles", font=("Arial", 10))
my_label.grid(column=3, row=0)

my_label = Label(text="is equal to ", font=("Arial", 10))
my_label.grid(column=0, row=1)

my_label = Label(text="Km", font=("Arial", 10))
my_label.grid(column=2, row=1)

my_label = Label(text="   0  ", font=("Arial", 10))
my_label.grid(column=1, row=1)

def Calculate():
    miles = float(input.get())
    km = miles * 1.60934
    my_label = Label(text=f"{int(km)}", font=("Arial", 10))
    my_label.grid(column=1, row=1)


button = Button(text="Calculate", command=Calculate)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)
input.get()




window.mainloop()