from tkinter import *
from PIL import ImageTk, Image

#
pizza = Tk()
pizza.geometry("1200x700")
pizza.title("My Pizza Ordering App")

# create labels
name_label = Label(pizza, text="Enter your name: ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=20)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="Enter your address: ")
address_label.grid(row=0, column=3)

address_entry = Entry(pizza, width=20)
address_entry.grid(row=0, column=4)

phone_label = Label(pizza, text="Enter your phone number: ")
phone_label.grid(row=0, column=5)

phone_entry = Entry(pizza, width=20)
phone_entry.grid(row=0, column=6)

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

my_pizza_list = ["Pepperoni", "Cheese", "Mushrooms", "Steak", "Olives"]

pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="purple")
pizza_list.grid(row=4, column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)

my_drinks_list = ["Pepsi", "Coca", "Corona", "Stella"]

drinks_list = Listbox(pizza, selectmode=MULTIPLE, bg="red")
drinks_list.grid(row=4, column=3)

for drink in my_drinks_list:
    drinks_list.insert(0, drink)


def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text="Your topping selection: " + "\n" + result)


def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text="Address: " + text2)
    new_lbl2.grid(row=5, column=3)

    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone: " + text3)
    new_lbl3.grid(row=5, column=4)


add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

add_button = Button(pizza, text="Add Topping", command=add_pizza)
add_button.grid(row=2, column=11)

check_button = Button(pizza, text="Checkout", command=check)
check_button.grid(row=3, column=11)

mainloop()
