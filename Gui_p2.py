from tkinter import *
import tkinter.font as font
import backend_db as backend

root=Tk()

#functions/db functions_______________________________________
def get_selected_row(event):
    global selected_record
    try:
        index=list1.curselection()[0]
        selected_record=list1.get(index)
        #print(type(selected_record[1]))
        

        E1.delete(0, END)
        E1.insert(END, selected_record[1])

        return selected_record[0]
    except:
        pass
def view_command():
    list1.delete(0, END)
    for row in backend.view_locations():
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    print(location_text.get())
    backend.insert_location(location_text.get())

def delete_command():
    backend.delete_location(selected_record[0])

def page1_command():
    root.destroy()
    import Gui

#Gui section _____________________________________________________________
buttonFont=font.Font(size="15", family="Arial")
L1 = Label(root, text="Log Location", font=("Courier", 25), bg="#B8894A")
L1.grid(row=1, column=2, ipadx=30)

#entrys
location_text=StringVar()
E1=Entry(root, textvariable=location_text, font=("Helvectica", 20))
E1.grid(row=2, column=2, ipadx=30)

#buttons___________________________________________________________________
b1=Button(root, text="View all", width=12, height=2,font=buttonFont, bg="blue",fg="white",command=view_command)
b1.grid(row=4, column=3)

b2=Button(root, text="Add Entry", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=insert_command)
b2.grid(row=5, column=3, pady=0)

delete_button=Button(root, text="Delete Selected", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=delete_command)
delete_button.grid(row=6, column=3)

b6=Button(root, text="Close",height=2, width=12,font=buttonFont, bg="blue",fg="white", command=root.destroy)
b6.grid(row=7, column=3)

infoFont=font.Font(size="15", family="Arial", weight="bold")
l2=Label(root, text="* this scan results will be written to locations in list", fg="red",bg="#B8894A")
l2.grid(row=8, column=2)
l2.config(font=infoFont)

page1=Button(root, text="Go to main page", height=2, width=25,font=buttonFont, bg="blue",fg="white",  command=page1_command)
page1.grid(row=9, column=2)


#_________________________________________________________________________________________________

list1 = Listbox(root, height=10, width=30,font=("Helvectica", 20))
list1.grid(row=4, column=2, rowspan=5, padx=25, pady=50)

list1.bind('<<ListboxSelect>>', get_selected_row)

root.title("Server Scanner")
root.geometry("900x850")
root.configure(bg="#B8894A")
root.mainloop()