def waiting():
    print("...")

def print_in_box(text: str) -> None:
    margin_width = 2
    horizontal_border_char = '='
    vertical_border_char = '|'

    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)
    max_line_length += 2 * margin_width

    # Prints the top border
    print(vertical_border_char + horizontal_border_char * max_line_length +
          vertical_border_char)

    # Prints each line with margins
    for line in lines:
        left_margin = (max_line_length - len(line)) // 2
        right_margin = max_line_length - (len(line) + left_margin)
        print(
            f"{vertical_border_char}{' ' * left_margin}{line}{' ' * right_margin}{vertical_border_char}"
        )

    # Print the bottom border
    print(vertical_border_char + horizontal_border_char * max_line_length +
          vertical_border_char)


# Start of the program
print_in_box("Hey, welcome to my coffee shoppe")
name = input("What is your name? ")
waiting()
print(f"Well {name}, it's nice to meet you!")
waiting()

while True:
    decision = input("Would you like to order now? (yes/no): ").lower()
    if decision in ('yes', 'y'):
        break
    elif decision in ('no', 'n'):
        print("No worries, take your time!")
        waiting()
        exit()
    else:
        print("Please enter 'yes' or 'no'.")

currency = input("What currency would you like to use? USD, EUR, or XMR?: ")
waiting()

menu = {
    1: ("Coffee", 2),
    2: ("Green Tea", 3),
    3: ("Root Beer", 4),
    4: ("Water", 1),
    5: ("Juice", 3),
    6: ("Soda", 2),
    7: ("Milk", 2),
    8: ("Americano", 3),
    9: ("Cappuccino", 4),
    10: ("Latte", 5),
    11: ("Meth :3", 1000),
    12: ("Rakija", 4),
}

if currency == "USD":
    menu_text = "\n".join(f"{num}. {item} - {price} {currency}"
                          for num, (item, price) in menu.items())
    print_in_box(f"Here's our menu:\n\n{menu_text}")
if currency == "EUR":
    menu_text = "\n".join(f"{num}. {item} - {price - 0.03} {currency}"
                          for num, (item, price) in menu.items())
    print_in_box(f"Here's our menu:\n\n{menu_text}")
if currency == "XMR":
    menu_text = "\n".join(f"{num}. {item} - {price / 195.41} {currency}"
                          for num, (item, price) in menu.items())
    print_in_box(f"Here's our menu:\n\nAll servings are 16oz\n\n{menu_text}")
    
waiting()

while True:
    try:
        choice = int(
            input(
                "Select a drink by entering the corresponding number (1-12): ")
        )
        if choice in menu:
            selected_item, price = menu[choice]
            if currency == "USD":
                print(
                    f"Great choice, {name}! You've selected {selected_item} for {price} {currency}. Enjoy your drink!"
                )
            if currency == "EUR":
                print(
                    f"Great choice, {name}! You've selected {selected_item} for {price - 0.03} {currency}. Enjoy your drink!"
                )
            if currency == "XMR":
                print(
                    f"Great choice, {name}! You've selected {selected_item} for {price / 195.41} {currency}. Enjoy your drink!"
                )
            break
        else:
            print("Try reading. idiot.")
    except ValueError:
        print("Invalid input. Please enter a number... idiot.")
