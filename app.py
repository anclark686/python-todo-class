from todo_list import TodoList

new_list = TodoList("New To Do List")

instructions = [
  "add - add a new item to your To Do list",
  "view - print a list of your existing To Do list items",
  "change - change the status of an existing To Do list item",
  "remove - remove an existing To Do item from your list",
  "end - end the session"
]

def make_a_selection():
  print()
  print("Please make a selection")
  print("*********************************************************")
  print("\n".join(instructions))
  print("*********************************************************")
  print()

print("Welcome to your new To Do list!")
make_a_selection()
selection = input("Enter selection: ").lower()

while selection != "end":

  if selection == "add":
    name = input("Please enter a name: ")
    desc = input("Please enter a description: ")
    print()
    new_list.add_todo({"name": name, "description": desc})
    print("Here's a list of your current To Do list:")
    print("*********************************************************")
    new_list.print_todos()
    print()
    cont = input("Type any key to continue")
  elif selection == "view":
    print()
    new_list.print_todos()
    print()
    cont = input("Type any key to continue")
  elif selection == "change":
    name = input("Enter the name of the To Do item you'd like to change: ")
    print()
    print(new_list.change_status(name))
    print()
    cont = input("Type any key to continue")
  elif selection == "remove":
    name = input("Enter the name of the To Do item you'd like to remove: ")
    print()
    print(new_list.remove_todo("name"))
    print()
    cont = input("Type any key to continue")
  else:
    print("Unable to determine your selection")
    print()
    cont = input("Type any key to continue")
  
  make_a_selection()
  selection = input("Enter selection: ").lower()