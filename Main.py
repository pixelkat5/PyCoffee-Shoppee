from art import *
randart("hellooo")
def waiting():
    print("...")

def print_in_box(text: str) -> None:
    """Print multi-line text in a box."""
    margin_width = 2
    horizontal_border_char = '='
    vertical_border_char = '|'

    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)

    max_line_length += 2 * margin_width
    horizontal_border = (
        vertical_border_char +
        horizontal_border_char * max_line_length +
        vertical_border_char
        )

    print(horizontal_border)

    for line in lines:
        # Calculate margin widths.
        left_margin = (max_line_length - len(line)) // 2
        right_margin = max_line_length - (len(line) + left_margin)

        formatted_line = (
            f"{vertical_border_char}"
            f"{' ' * left_margin}{line}{' ' * right_margin}"
            f"{vertical_border_char}"
            )

        print(formatted_line)

    print(horizontal_border)

def print_box(text):
    """outputs a box around the text"""
    lines = text.splitlines()
    max_length = max(len(line) for line in lines)
    print("-" * (max_length + 4))
    for line in lines:
        print("| " + line.ljust(max_length) + " |")
    print("~" * (max_length + 4))


print_in_box("Hey, welcome to my coffee shoppe")
# print_box("Hey, welcome to my coffee shoppe")

name = input('what is your name? ')
waiting()

print(f"well {name}, its nice to meet you ")
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

print_in_box("""Here's our menu:\n
 1. Coffee ☕️ 
 2. Green Tea 
 3. Root Beer 
 4. Water  
 5. Juice
 6. Soda
 7. Milk
 8. Americano
 9. Cappuccino
 10. Latte""")
waiting()
input()
