# To Do List App

from customtkinter import *
from datetime import datetime

set_appearance_mode("dark")
set_default_color_theme("dark-blue")
class App:
  tasks_id = 0
  def __init__(self):
    self.app = CTk()
    self.app.geometry("600x600")
    self.app.title("To Do List App")
    self.app.resizable(True, True)
    self.tasks = [{"id":100, "task":"Do something1", "time":"1/1/2000, 1:00 AM", "showen":True}, {"id":101, "task":"Do something", "time":"1/1/2000, 1:00 AM", "showen":False}]
    self.lbl_tasks = []
    self.app.iconbitmap("todoicon.ico")
    self.date_label = CTkLabel(self.app, 
    font=("Arial", 20))
    self.task_entry = CTkEntry(self.app, 
    width=580, 
    height=50, 
    placeholder_text=" Enter task", 
    font=("Arial", 18))
    self.submit_button = CTkButton(self.app, 
    text="Submit", 
    command=self.append_task, 
    height=40, 
    font=("Arial", 18))

    self.canvas_frame = CTkFrame(self.app, width=600, height=400, fg_color="transparent")

    self.canvas = CTkCanvas(self.canvas_frame, width=580, height=400, bg="grey20", highlightthickness=0)

    self.scrollbar = CTkScrollbar(self.canvas_frame, orientation="vertical", command=self.canvas.yview)

    self.main_frame = CTkFrame(self.canvas, width=580, height=400, fg_color="transparent")

  def show_entry(self):
    # entry in the buttom of window
    self.submit_button.pack(side="bottom", pady=10)
    self.task_entry.pack(side="bottom", pady=10) 

  def show_tasks(self):
    for task in self.tasks:
      if not task["showen"]:
      # create a label for each task aligned to the left
        task["showen"] = True
        task_frame = CTkFrame(self.main_frame, width=500)
        task_frame.pack(side="top", fill="both", padx=5, pady=5)
        task_name = CTkLabel(task_frame, text=task["task"], font=("Arial", 20), width=575)
        task_name.pack(side="top",  fill="both")
        task_time = CTkLabel(task_frame, text=task["time"], font=("Arial", 12) )
        task_time.pack(side="top", fill="both")
        self.lbl_tasks.append({"id": task["id"],"task":task_frame})

  def append_task(self):
    task = self.task_entry.get()
    time = datetime.now().strftime("%B %d, %Y \n%I:%M %p")
    App.tasks_id += 1
    self.show_tasks()

    self.tasks.append({
      "id": App.tasks_id,
      "task": task,
      "time": time,
      "showen": False
    })
    self.task_entry.delete(0, "end")
    self.show_tasks()

  def delete_task(self):
    pass

  def edit_task(self):
    pass

  def get_stored_tasks(self):
    pass

  def update_date(self):
    now = datetime.now()
    date = now.strftime("%B %d, %Y \n%I:%M %p")
    self.date_label.configure(text=date)
    self.date_label.after(1000, self.update_date)

  def get_entry(self):
    pass
def on_frame_configure(event):
    app.canvas.configure(scrollregion=app.canvas.bbox("all"))
app = App()

app.date_label.pack(pady=10)
app.canvas_frame.pack(side="top", fill="both", expand=True)
app.canvas.pack(side="left", fill="both", expand=True)
app.scrollbar.pack(side="right", fill="y")
app.canvas.configure(yscrollcommand=app.scrollbar.set)
app.canvas.create_window((0, 0), window=app.main_frame, anchor="nw")
app.main_frame.bind("<Configure>", lambda e: app.canvas.configure(scrollregion=app.canvas.bbox("all")))
app.show_tasks()
app.update_date()
app.show_entry()
app.app.mainloop()
