import sqlite3

db = sqlite3.connect("tasks.db")
cr = db.cursor()

# Create Table If Not Exists
def create_db():
  cr.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER KEY, task TEXT, date TEXT, done INTEGER)")

# Get All Stored Tasks
def get_tasks_db():
  cr.execute("SELECT * FROM tasks")
  return cr.fetchall()

# Add New Task
def add_tasks_db(id, task, date, done):
  cr.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)", (id, task, date, done))
  commit_db()

# Edit Task Name
def edit_task_name_db(task, id):
  cr.execute("UPDATE tasks SET task = ?  WHERE id = ?", (task, id))
  commit_db()

# Edit Task State
def edit_state_db(done, id):
  cr.execute("UPDATE tasks SET done = ?  WHERE id = ?", (done, id))
  commit_db()

# Delete Task
def delete_task_db(id):
  cr.execute("DELETE FROM tasks WHERE id = ?", (id,))
  commit_db()

# Commit Changes To Database
def commit_db():
  db.commit()

# Close Database
def close_db():
  db.close()