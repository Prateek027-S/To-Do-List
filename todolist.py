#Listbox widget, scrollbar widget
from tkinter  import *
from tkinter import messagebox
import pickle

def add_task(task):
    if len(task)==0:
        messagebox.showerror("Empty Field", "Please enter a task!")
    else:
        index = check_index(task)
        if index<0:
            Lbox.insert(END, task)
        else:
            messagebox.showerror("Error",  "This task is already present in the List")

def check_index(element):
   try:
       index = Lbox.get(0, "end").index(element)
   except ValueError:
       index = -1
   return index

def delete_task():
    try:
        index = Lbox.curselection()[0]
        Lbox.delete(index)
    except:
        messagebox.showerror("Error", "Please select a task to be deleted.")

def save_tasks():
    tasks=Lbox.get(0, Lbox.size())
    pickle.dump(tasks, open("Tasks.dat", "wb"))

def load_tasks():
    try:
        tasks = pickle.load(open("Tasks.dat", "rb"))
        Lbox.delete(0, END)
        for task in tasks:
            Lbox.insert(END, task)
    except:
        messagebox.showerror("Error", "No saved tasks were found!")

def clear():
    if Lbox.size()==0:
        messagebox.showinfo("Already empty", "The List is already empty!")
    else:
        ans = messagebox.askquestion("WARNING", "You are about to delete all the tasks in the List. Do you wish to continue?", icon='warning')
        if ans=='yes':
            Lbox.delete(0, END)
        else:
            messagebox.showinfo("Deletion Unsuccessful", "No items were deleted")

win = Tk()
win.title("To Do List")
'''win.geometry('400x300')
win.maxsize(400, 300)
win.minsize(400, 300)'''
frame1 = Frame(win)
frame1.pack()
Lbox = Listbox(frame1, height=15, width=50)
Lbox.pack(side=LEFT)
scrlbar = Scrollbar(frame1)
scrlbar.pack(side=RIGHT, fill=Y)
Lbox.config(yscrollcommand=scrlbar.set)
scrlbar.config(command=Lbox.yview)
task = StringVar()
task.set("<Enter your task here to be added in the List>")
E_task = Entry(win, textvariable=task, width=48)
E_task.pack(pady=10)
Button(win, text="Add Task", cursor="hand2", command=lambda: add_task(E_task.get()), fg='white', bg='#3895D3', border=4, font=("Roboto Mono", 12), width=20).pack(pady=5)
Button(win, text="Delete Selected Task", cursor="hand2", command=delete_task, fg='white', bg='#3895D3', border=4, font=("Roboto Mono", 12), width=20).pack(pady=5)
Button(win, text="Clear List", cursor="hand2", command=clear, fg='white', bg='#3895D3', border=4, font=("Roboto Mono", 12), width=20).pack(pady=5)
Button(win, text="Save all Tasks", cursor="hand2", command=save_tasks, fg='white', bg='#3895D3', border=4, font=("Roboto Mono", 12), width=20).pack(pady=5)
Button(win, text="Load saved Tasks", cursor="hand2", command=load_tasks, fg='white', bg='#3895D3', border=4, font=("Roboto Mono", 12), width=20).pack(pady=5)
win.mainloop()
