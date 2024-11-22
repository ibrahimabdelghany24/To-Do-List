from ToDoList import *

create_db()
app = App()
app.show_date()
app.show_main_frame()
app.show_tasks()
app.update_date()
app.show_entry()
app.mainloop()
close_db()