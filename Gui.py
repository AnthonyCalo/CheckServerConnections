from tkinter import *
import tkinter.font as font
import backend_db as backend
import CheckServer
from tkinter import ttk
root =Tk()
backend.connect()

#functions/db functions_______________________________________
def run_scan():
    serverList=[]
    for row in backend.view_servers():
        #minor difference is that 3, 2 are swapped because connnection and port are in diff orders in db vs
        #server class
        serverList.append(CheckServer.Server(row[1],row[3],row[2],row[4]))
    for server in serverList:
        server.check_connection()
def get_selected_row(event):
    global selected_record
    try:
        index=list1.curselection()[0]
        selected_record=list1.get(index)
        #print(type(selected_record[1]))
        

        E1.delete(0, END)
        E1.insert(END, selected_record[1])
        # E2.delete(0, END)
        # E2.insert(END, selected_record[2])
        connection_text.set(selected_record[2])
        E3.delete(0, END)
        E3.insert(END, selected_record[3])
        priority_text.set(selected_record[4])
        return selected_record[0]
    except:
        pass

def delete_command():
    backend.delete(selected_record[0])

def view_command():
    list1.delete(0, END)
    for row in backend.view_servers():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(URL_text.get(), connection_text.get(), port_text.get(), priority_text.get()):
        list1.insert(END, row)

def insert_command():
    list1.delete(0, END)
    print(priority_text)
    print(priority_text.get(), "<-.current")
    backend.insert(URL_text.get(), connection_text.get(), port_text.get(), priority_text.get())

def update_command():
    backend.update(selected_record[0], URL_text.get(), connection_text.get(), port_text.get(), priority_text.get())

def page2_command():
    root.destroy()
    import Gui_p2

#hover command
def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,
        fg='white'
        ))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


#Gui section _____________________________________________________________
buttonFont=font.Font(size="15", family="Arial")
dropFont=font.Font(size="20", family="Helvectica")

L1 = Label(root, text="URL", font=("Courier", 25), bg="#B8894A")
L1.grid(row=1, column=2, padx=25)

L2 = Label(root, text="Connection Type", font=("Courier", 25), bg="#B8894A")
L2.grid(row=3, column=2, padx=25)

L3 = Label(root, text="Port", font=("Courier", 25), bg="#B8894A")
L3.grid(row=1, column=6, padx=50)

L4 = Label(root, text="Priority", font=("Courier", 25), bg="#B8894A")
L4.grid(row=3, column=6, padx=50)

#entrys
URL_text=StringVar()
E1=Entry(root, textvariable=URL_text, font=("Helvectica", 20))
E1.grid(row=2, column=2, padx=25)

connection_text=StringVar()
connection_list=("plain", "ssl", "ping", " ")

# E2=Entry(root, textvariable=connection_text, font=("Helvectica", 20))
# E2.grid(row=4, column=2, padx=25)
connection_text.set("plain")
e2_dropdown=ttk.Combobox(root, values=connection_list, textvariable=connection_text)
e2_dropdown.set(connection_text)
e2_dropdown.config(width=18, height=1, font=dropFont)
e2_dropdown['state']="readonly"
e2_dropdown.grid(row=4, column=2) 


port_text=StringVar()
E3=Entry(root, textvariable=port_text, font=("Helvectica", 20))
E3.grid(row=2, column=6, padx=25)


priority_text=StringVar()
priority_list=("high", "low")
# E4=Entry(root, textvariable=priority_text, font=("Helvectica", 20))
# E4.grid(row=4, column=6, padx=25)
e4_dropdown=ttk.Combobox(root, values=priority_list, textvariable=priority_text)
e4_dropdown.set(priority_text)
e4_dropdown.config(width=18, height=1, font=dropFont)
e4_dropdown['state']="readonly"
e4_dropdown.grid(row=4, column=6) 

list1 = Listbox(root, height=15, width=30,font=("Helvectica", 20))
list1.grid(row=5, column=2, rowspan=6, columnspan=5,padx=25, pady=50)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1=Button(root, text="View all", width=12, height=2,font=buttonFont, bg="blue",fg="white",command=view_command)
b1.grid(row=5, column=7)

b2=Button(root, text="Search Entry", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=search_command)
b2.grid(row=6, column=7)

b3=Button(root, text="Add Entry", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=insert_command)
b3.grid(row=7, column=7, pady=0)

b4=Button(root, text="Update select", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=update_command)
b4.grid(row=8, column=7)

b5=Button(root, text="Delete Selected", width=12, height=2, font=buttonFont, bg="blue",fg="white", command=delete_command)
b5.grid(row=9, column=7)

b6=Button(root, text="Close",height=2, width=12,font=buttonFont, bg="blue",fg="white", command=root.destroy)
b6.grid(row=10, column=7)

b7=Button(root, text="Run Scan", height=2, width=25,font=buttonFont, bg="blue",fg="white",  command=run_scan)
b7.grid(row=11, column=2)

b8=Button(root, text="Change output location", height=2, width=25,font=buttonFont, bg="blue",fg="white",  command=page2_command)
b8.grid(row=11, column=6)

changeOnHover(b1, "green", "blue")
changeOnHover(b2, "green", "blue")
changeOnHover(b3, "green", "blue")
changeOnHover(b4, "green", "blue")
changeOnHover(b5, "green", "blue")
changeOnHover(b5, "green", "blue")
changeOnHover(b6, "green", "blue")
changeOnHover(b7, "green", "blue")
changeOnHover(b8, "green", "blue")

root.title("Server Scanner")
root.geometry("900x850")
root.configure(bg="#B8894A")
root.mainloop()
