from tkinter import *
import Back_End

def get_selected_row(event):
    global selected_tuple #create global variable
    index = list1.curselection()[0] #curselection used to get the index of selected row in listbox
    selected_tuple = list1.get(index) #from listbox get the tuple with specific index
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0, END) #deletes everything from index 0 to end of last row
    for row in Back_End.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in Back_End.search(title_text.get(),  author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    Back_End.insert(title_text.get(),  author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(),  author_text.get(), year_text.get(), isbn_text.get())) #shows values user entered in listbox

def delete_command():
    Back_End.delete(selected_tuple[0])

def update_command():
    Back_End.update(selected_tuple[0], title_text.get(),  author_text.get(), year_text.get(), isbn_text.get())

window = Tk()

window.wm_title('BookStore') #title of window

l1 = Label(window, text = 'Title')
l1.grid(row = 0, column = 0)

l2 = Label(window, text = 'Year')
l2.grid(row = 1, column = 0)

l3 = Label(window, text = 'Author')
l3.grid(row = 0, column = 2)

l4 = Label(window, text = 'ISBN')
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35) #list box for the output
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2) #want to span over multiple rows and columns

sb1 = Scrollbar(window) #create scrollbar
sb1.grid(row=3,column = 2, rowspan = 4, sticky = 'ns')

list1.configure(yscrollcomman = sb1.set) #set scrollbar to listbox using vertical scroll
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row) #bind used to bind a function to a widget. takes an event type and a function

b1 = Button(window, text = 'View all', width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search entry', width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = 'Add entry', width = 12, command = insert_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = 'Update selected', width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = 'Delete selected', width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = 'Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
