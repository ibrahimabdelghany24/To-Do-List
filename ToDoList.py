# To Do List App
# remember to do database with sqlite3
import sqlite3
from customtkinter import *
from tkinter import  Menu
from datetime import datetime

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class App(CTk):
  tasks_id = 0
  def __init__(self):
    super().__init__()
    self.geometry("600x600")
    self.title("To Do List App")
    self.resizable(True, True)
    self.tasks = {
      1: {"task": "Task 1", "time": "Task 1 time", "done": False},
      2: {"task": "Task 1", "time": "Task 1 time", "done": False},
      3: {"task": "Task 1", "time": "Task 1 time", "done": False},
    }
    self.frame_tasks = {}
    self.iconbitmap("todoicon.ico")
    self.date_label = CTkLabel(self, 
    font=("Arial", 20))
    self.task_entry = CTkEntry(self, 
    width=580, 
    height=50, 
    placeholder_text=" Enter task", 
    font=("Arial", 18))
    self.submit_button = CTkButton(self, 
    text="Submit", 
    command=self.append_task, 
    height=40, 
    font=("Arial", 18))
    self.scrollable_frame = CTkScrollableFrame(self, width=500, height=350)

  def show_entry(self):
    # entry in the buttom of window
    self.submit_button.pack(side="bottom", pady=10)
    self.task_entry.pack(side="bottom", pady=10) 

  def append_task(self):
    task = self.task_entry.get()
    time = datetime.now().strftime("%B %d, %Y   %I:%M %p")
    App.tasks_id = len(self.tasks) + 1

    self.tasks[app.tasks_id] = {
      "task": task,
      "time": time,
      "done": False
    }
    self.task_entry.delete(0, "end")
    self.show_one_task(App.tasks_id, self.tasks[App.tasks_id])


  def delete_task(self, task_id):
        self.frame_tasks[task_id]["frame"].destroy()
        self.frame_tasks.pop(task_id)
        self.tasks.pop(task_id)

  def edit_task(self, task_id):
        dialog = CTkInputDialog(text="Edit Task", title="Test")
        text = dialog.get_input() 
        self.frame_tasks[task_id]["task_label"].configure(text=text)
        self.tasks[task_id]["task"] = text

  def get_stored_tasks(self):
    pass

  def update_date(self):
    now = datetime.now()
    date = now.strftime("%B %d, %Y \n%I:%M %p")
    self.date_label.configure(text=date)
    self.date_label.after(1000, self.update_date)

  def show_one_task(self, id, task):
    frame = CTkFrame(app.scrollable_frame, corner_radius=5)
    label = CTkLabel(frame,padx = 10,pady=10, text=task["task"], font=("Arial", 20), width= 580, anchor="w", bg_color="#333c4d")
    label2 = CTkLabel(frame, padx = 10,pady=10,text=task["time"], font=("Arial", 16), width= 580, anchor="e", bg_color="#333c4d")
    label.pack()
    label2.pack()
    frame.pack(pady=5, fill="both", expand=True)
    self.frame_tasks[id] = {"task_label":label,"date_label":label2, "frame":frame}
    label.bind("<Button-3>", lambda event, task_id=id: self.show_context_menu(event, task_id))
    label2.bind("<Button-3>", lambda event, task_id=id: self.show_context_menu(event, task_id))

  def show_tasks(self):
    for id, task in self.tasks.items():
      self.show_one_task(id, task)
      if task["done"]:
        self.frame_tasks[id]["task_label"].configure(text_color="#515a5a")
        self.frame_tasks[id]["date_label"].configure(text="Done")

  def show_context_menu(self,event, task_id):
    menu = Menu(self, tearoff=0)
    menu.add_command(label="Done", command=lambda task_id=task_id: self.task_done(task_id))
    menu.add_command(label="Edit", command=lambda task_id=task_id: self.edit_task(task_id))
    menu.add_separator()
    menu.add_command(label="Delete",command=lambda task_id=task_id: self.delete_task(task_id))
    menu.post(event.x_root, event.y_root)

  def task_done(self, task_id):
    self.frame_tasks[task_id]["task_label"].configure(text_color="#515a5a")
    self.frame_tasks[task_id]["date_label"].configure(text="Done")



app = App()
app.date_label.pack(pady=10, side="top")
app.scrollable_frame.pack(side="top", fill="both", expand=True)
app.show_tasks()
app.update_date()
app.show_entry()
app.mainloop()
