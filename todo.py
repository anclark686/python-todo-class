class Todo():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.done = False

  def show_details(self):
    status = "done" if self.done else "incomplete"
    return f"description = {self.description}; status = {status}"
  
  def change_status(self):
    self.done = not self.done