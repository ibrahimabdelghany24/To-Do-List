# To Do List App
from database import *
from customtkinter import *
from tkinter import  Menu
from datetime import datetime
from pygame import mixer

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class App(CTk):
  tasks_id = 0
  def __init__(self):
    super().__init__()
    mixer.init()
    self.geometry("600x600")
    self.title("To Do List App")
    self.resizable(True, True)
    self.tasks = {
    }
    self.get_stored_tasks()
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
# Sounds Methods
  def done_sound(self):
    mixer.Sound("./Sounds/done.mp3").play()

  def delete_sound(self):
    mixer.Sound("./Sounds/deletion.mp3").play()
# Show Methods
  def show_entry(self):
    # entry in the buttom of window
    self.submit_button.pack(side="bottom", pady=10)
    self.task_entry.pack(side="bottom", pady=10) 

  def show_main_frame(self):
    self.scrollable_frame.pack(side="top", fill="both", expand=True)
    self.date_label.pack(pady=10, side="top")

  def show_date(self):
    self.date_label.pack(pady=10, side="top")

  def show_one_task(self, id, task):
    frame = CTkFrame(self.scrollable_frame, corner_radius=5)
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
        self.frame_tasks[id]["date_label"].configure(text="Done✅")

  def show_context_menu(self, event, task_id):
    menu = Menu(self, tearoff=0)
    menu.add_command(label=f"{"Done" if not self.tasks[task_id]['done'] else "Undone"}", command=lambda task_id=task_id: self.task_done(task_id))
    menu.add_command(label="Edit", command=lambda task_id=task_id: self.edit_task(task_id))
    menu.add_separator()
    menu.add_command(label="Delete",command=lambda task_id=task_id: self.delete_task(task_id))
    menu.post(event.x_root, event.y_root)

# Append & Edit Methods
  def append_task(self):
    if self.task_entry.get() != "":
      task = self.task_entry.get()
      time = datetime.now().strftime("%B %d, %Y   %I:%M %p")
      if len(self.tasks):
        App.tasks_id = max(self.tasks.keys())
      App.tasks_id += 1

      self.tasks[App.tasks_id] = {
        "task": task,
        "time": time,
        "done": False
      }
      add_tasks_db(App.tasks_id, task, time, False)
      self.task_entry.delete(0, "end")
      self.show_one_task(App.tasks_id, self.tasks[App.tasks_id])

  def delete_task(self, task_id):
        self.frame_tasks[task_id]["frame"].destroy()
        self.delete_sound()
        self.frame_tasks.pop(task_id)
        self.tasks.pop(task_id)
        delete_task_db(task_id)

  def edit_task(self, task_id):
    dialog = CTkInputDialog(text="Edit Task", title="Edit")
    text = dialog.get_input() 
    if text: 
      self.frame_tasks[task_id]["task_label"].configure(text=text)
      self.tasks[task_id]["task"] = text
      edit_task_name_db(text, task_id)

  def update_date(self):
    now = datetime.now()
    date = now.strftime("%B %d, %Y \n%I:%M %p")
    self.date_label.configure(text=date)
    self.date_label.after(1000, self.update_date)

  def task_done(self, task_id):
    self.tasks[task_id]["done"] = not self.tasks[task_id]["done"]
    edit_state_db(self.tasks[task_id]["done"], task_id)
    if self.tasks[task_id]["done"]:
      self.done_sound()
      self.frame_tasks[task_id]["task_label"].configure(text_color="#515a5a")
      self.frame_tasks[task_id]["date_label"].configure(text="Done✅")
    else:
      self.frame_tasks[task_id]["task_label"].configure(text_color="white")
      self.frame_tasks[task_id]["date_label"].configure(text=self.tasks[task_id]["time"])

# Get Stored Tasks From Database
  def get_stored_tasks(self):
    data = get_tasks_db()
    for id, task, time, done in data:
      self.tasks[id] = {
      "task": task,
      "time": time,
      "done": done
    }



