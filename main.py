from tkinter import *
from PIL import ImageTk, Image

#
pizza = Tk()
pizza.geometry("1000x600")
pizza.title("My Pizza Ordering App")

# create labels
name_label = Label(pizza, text="Enter your name: ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=20)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="Enter your address: ")
address_label.grid(row=0, column=3)

name_entry = Entry(pizza, width=20)
name_entry.grid(row=0, column=4)

phone_label = Label(pizza, text="Enter your phone number: ")
phone_label.grid(row=0, column=5)

name_entry = Entry(pizza, width=20)
name_entry.grid(row=0, column=6)

my_pic = Image.open("pizza1.jfif")
resized = my_pic.resize((320, 200), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

my_label = Label(image=new_pic)
my_label.grid(row=4, column=0)

# Adding pictures and resizing them
my_pic_2 = Image.open("Pizza_High_quality_wallpapers0.jpg")
resized_2 = my_pic_2.resize((320, 200), Image.ANTIALIAS)
new_pic_2 = ImageTk.PhotoImage(resized_2)

my_label = Label(image=new_pic_2)
my_label.grid(pady=70)

button_exit = Button(pizza, text="Exit", command=pizza.quit)
button_exit.grid(row=300, column=100)

top = Toplevel()
lbl = Label(top, text="Hello world").grid()

# button_check = Button(pizza, text="CheckOut", command=check)
# button_check.grid(row=10,column=10)
pizza.mainloop()
