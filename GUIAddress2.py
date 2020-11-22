from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from GUIAddress1 import Database
root = Tk() #begin the app window
root.title("Address Book") #App title
#root.geometry('650x300')
#root.resizable(False, False)#makes the window not resizable

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='Tab 1') 
tabControl.add(tab2, text ='Tab 2') 
tabControl.pack(expand = 1, fill ="both")


#to create a table (Only use this once to create the table, comment it out later on)
#cursor.execute("""CREATE TABLE addresses(
 #           first_name text,
 #           last_name text,
 #           address text,
 #           city text,
 #           state text,
 #           pincode integer)
  #          """)
#Button Functions 





#trial

db = Database('address_book1.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if f_name.get() == '' or l_name.get() == '' or address.get() == '' or city.get() == '' or state.get() == '' or pincode.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(f_name.get(), l_name.get(), address.get(), city.get(), state.get(), pincode.get() )
    parts_list.delete(0, END)
    parts_list.insert(END, (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), pincode.get()))
    
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        f_name.delete(0, END)
        f_name.insert(END, selected_item[1])
        l_name.delete(0, END)
        l_name.insert(END, selected_item[2])
        address.delete(0, END)
        address.insert(END, selected_item[3])
        city.delete(0, END)
        city.insert(END, selected_item[4])
        state.delete(0, END)
        state.insert(END, selected_item[5])
        pincode.delete(0, END)
        pincode.insert(END, selected_item[6])
    except IndexError:
        pass


def remove_item():
    response = messagebox.askyesno("Remove Entry?", "Are you sure you want to delete the selected entry?")
    if response == 1:
        db.remove(selected_item[0])
        clear_text()
        populate_list()


def update_item():
    response = messagebox.askyesno("Update Entry?", "Are you sure you want to update the selected entry?")
    if response == 1:
        db.update(selected_item[0], f_name.get(), l_name.get(), address.get(), city.get(), state.get(), pincode.get())
        if f_name.get() == '' or l_name.get() == '' or address.get() == '' or city.get() == '' or state.get() == '' or pincode.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        populate_list()
        print("Working as Expected")


def clear_text():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    pincode.delete(0, END)









frame = Frame(tab1)
frame.grid(row = 4, column = 0, columnspan = 2, rowspan = 2,  padx = (20, 10))
# Create scrollbar
scrollbar = Scrollbar(frame, orient = VERTICAL)


# Parts List (Listbox)
parts_list = Listbox(frame, height=8, width=50,  yscrollcommand = scrollbar)
scrollbar.config(command=parts_list.yview)
scrollbar.pack(side = RIGHT, fill = Y)
parts_list.pack(pady = 15)

# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)


#Entry boxes for fields
f_name = Entry(tab1, width = 30)
f_name.grid(row = 0, column = 1, padx = 10, pady = 5)

l_name = Entry(tab1, width = 30)
l_name.grid(row = 0, column = 3, padx = 10, pady = 5)

address = Entry(tab1, width = 30)
address.grid(row = 1, column = 1, padx = 10, pady = 5)

city = Entry(tab1, width = 30)
city.grid(row = 1, column = 3, padx = 10, pady = 5)

state = Entry(tab1, width = 30)
state.grid(row = 2, column = 1, padx = 10, pady = 5)

pincode = Entry(tab1, width = 30)
pincode.grid(row = 2, column = 3, padx = 10, pady = 5)

#Labels for entry boxes
f_name_label = Label(tab1, text = 'First Name :')
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(tab1, text = 'Last Name :')
l_name_label.grid(row = 0, column = 2)

address_label = Label(tab1, text = 'Address :')
address_label.grid(row = 1, column = 0)

city_label = Label(tab1, text = 'City :')
city_label.grid(row = 1, column = 2)

state_label = Label(tab1, text = 'State :')
state_label.grid(row = 2, column = 0)

pincode_label = Label(tab1, text = 'Pincode :')
pincode_label.grid(row = 2, column = 2, padx = 15)

#buttons
btn_submit = Button(tab1, text = 'Add Entry', command = add_item)
btn_submit.grid(row = 4, column = 2 , padx = 5,pady = 5, ipadx = 20)

btn_delete = Button(tab1, text = 'Delete Entry', command = remove_item)
btn_delete.grid(row = 4, column = 3 , padx = 5,pady = 5, ipadx = 20)

btn_update = Button(tab1, text = 'Update Entry', command = update_item)
btn_update.grid(row = 5, column = 2 , padx = 5, pady = 5,ipadx = 20)

btn_clear = Button(tab1, text = 'Clear', command = clear_text)
btn_clear.grid(row = 5, column = 3 , padx = 5, pady = 5, ipadx = 20)


# Populate data
populate_list()






root.mainloop()