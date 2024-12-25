###age = input("Enter your age: ")
###age = int(age)  # Convert the input to an integer
###print("You will be", age + 1, "years old next year.")


def waiting():
  print("...")


def print_box(text):
  """Prints a box around the given text."""
  lines = text.splitlines()
  max_length = max(len(line) for line in lines)
  print("*" * (max_length + 4))
  for line in lines:
    print("* " + line.ljust(max_length) + " *")
  print("*" * (max_length + 4))


def split_lines(text):
  """Splits a string into a list of lines."""
  return text.splitlines()


print_box("hey, welcome to my coffee shoppe")

name = input('what is your name? ')
waiting()
print(f"well its nice to meet you, {name}")
waiting()

while True:
  decision = input("would you wish to order now? (yes/no) ").lower()
  if decision in ('yes', 'y', 'sure', 'yeah', 'okay'):
    break
  elif decision in ('n', 'no', 'nope', 'nah'):
    import time
    time.sleep(2)
  else:
    print("Please enter 'yes' or 'no'.")
waiting()
