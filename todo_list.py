from todo import Todo

class TodoList():
  def __init__(self, name):
    self.name = name
    self.todos = {}

  def add_todo(self, todo_dict):
    try:
      todo = Todo(todo_dict["name"], todo_dict["description"])
      self.todos[todo_dict["name"]] = todo
      print(f"Todo {todo_dict['name']} successfully added")
    except TypeError as err:
      print(f"Unable to add new todo: {todo_dict['name']}")
      print(err)
      
    return self.todos
  
  def add_mult_todos(self, *args):
    errs = []
    for todo in args:
      try:
        new_todo = Todo(todo["name"], todo["description"])
        self.todos[todo["name"]] = new_todo
        print(f"Todo {todo['name']} successfully added")
      except TypeError:
        errs.append(todo['name'])

    if errs:
      print(f"Unable to add the following items: {', '.join(errs)}")

    return self.todos

  def print_todos(self):
    for key, todo in self.todos.items():
      print(f"{key}: {todo.show_details()}")

  def change_status(self, todo_name):
    try:
      todo = self.todos[todo_name]
      todo.change_status()
      return todo.show_details()
    except KeyError:
      return f"Unable to locate todo with number: {todo_name}"
  
  def remove_todo(self, todo_name):
    try:
      del self.todos[todo_name]
      return f"Successfully removed {todo_name}"
    except KeyError:
      return f"Unable to locate todo with number: {todo_name}"
