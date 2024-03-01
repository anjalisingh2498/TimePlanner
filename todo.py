import tkinter as tk
from tkinter import simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title('Task Manager')


        self.todo_list = tk.Listbox(master, height=30, width=60)
        self.todo_list.pack(side=tk.LEFT, padx=10, pady=10)
        self.todo_list.configure(background="cadetblue", foreground="white", font=('Aerial 20'))

        self.add_button = tk.Button(master, text='Add', command=self.add_item,font=('Arial', 12),background='cadetblue',foreground='white')
        self.add_button.pack(side=tk.TOP,pady=50)

        self.remove_button = tk.Button(master, text='Remove', command=self.remove_item, font=('Arial', 12),background='cadetblue',foreground='white')
        self.remove_button.pack(side=tk.TOP,pady=50)

        self.clear_button = tk.Button(master, text='Clear All', command=self.clear_items,font=('Arial', 12),background='cadetblue',foreground='white')
        self.clear_button.pack(side=tk.TOP,pady=50)

        self.quit_button = tk.Button(master, text='Quit', command=master.quit,font=('Arial', 12),background='cadetblue',foreground='white')
        self.quit_button.pack(side=tk.TOP,pady=50)
        self.master['bg'] = 'white'

    def add_item(self):
        new_item = tk.simpledialog.askstring('Add Item', 'Enter new item:')
        if new_item:
            self.todo_list.insert(tk.END, new_item)

    def remove_item(self):
        selected_items = self.todo_list.curselection()
        for item in selected_items:
            self.todo_list.delete(item)

    def clear_items(self):
        self.todo_list.delete(0, tk.END)


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
