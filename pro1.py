import tkinter as tk
import sys
def add_activity():
    activity = entry_activity.get()
    if activity:
        listbox_data.insert(tk.END, activity)
        entry_activity.delete(0, tk.END)
def remove_activity():
    selected_index = listbox_data.curselection()
    if selected_index:
        listbox_data.delete(selected_index)


def remove_all():
    listbox_data.delete(0, tk.END)

def exit_activity():
    sys.exit()

root = tk.Tk()
root.title("Todo List")

# Create GUI components
label_heading = tk.Label(root, text="TODO LIST", font=("Algerian", 40, "bold"),
                         width=20, height=1, bd=5, bg='light blue', highlightbackground='black', fg='black')
label_heading.pack()

entry_activity = tk.Entry(root, width=40,font=("Helvetica", 20), bd=5)
entry_activity.pack()

button_add = tk.Button(root, text="Add",font=("Helvetica", 16, "bold"), command=add_activity,width=10,
                       height=1, bd=5, bg='green', fg='black')
button_add.pack()

listbox_data = tk.Listbox(root, selectmode=tk.SINGLE, width=60,font=("Helvetica", 18),bd=5,height=10, bg='grey', fg='black')
listbox_data.pack()

button_remove = tk.Button(root, text="Remove", font=("Helvetica", 12,"bold"), command=remove_activity, width=9, height=1,
                          bd=5, bg='skyblue', fg='black')
button_remove.pack()

button_remove_all = tk.Button(root, text="Remove All", font=("Helvetica", 12,"bold"), command=remove_all,
                              width=9, height=1, bd=5,
                              bg='skyblue', fg='black')
button_remove_all.pack()
button_exit = tk.Button(root, text="Exit", font=("Helvetica", 12,"bold"), command=exit_activity ,
                              width=9, height=1, bd=5,
                              bg='skyblue', fg='black')
button_exit.pack()

root.mainloop()