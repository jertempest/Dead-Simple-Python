# lunch_order = input("What do you what for lunch? ").lower().strip()

# match lunch_order:
#     case 'pizza':
#         print("Pizza time!")
#     case 'sandwich':
#         print("Here's your sandwich.")
#     case 'taco':
#         print("Taco, taco, TACO, tacotacotaco!")
#     case _:
#         print("Yummy")

# lunch_order = input("What do you what for lunch? ").lower().strip()

# match lunch_order:
#     case 'taco':
#         print("Taco, taco, TACO, tacotacotaco!")
#     case 'salad' | 'soup':
#         print("Eating healthy eh?")
#     case _:
#         print("Yummy")

# lunch_order = input("What do you what for lunch? ").lower().strip()

# match lunch_order:
#     case "taco":
#         print("Taco, taco, TACO, tacotacotaco!")
#     case "salad" | "soup":
#         print("Eating healthy eh?")
#     case order:
#         print(f"Enjoy your {order}.")

# lunch_order = input("What do you what for lunch? ").lower().strip()

# if " " in lunch_order:
#     lunch_order = lunch_order.split(maxsplit=1)

# match lunch_order:
#     case (flavour, 'ice cream'):
#         print(f"Here's your very grown_up {flavour}...lunch")
#     case "taco":
#         print("Taco, taco, TACO, tacotacotaco!")
#     case "salad" | "soup":
#         print("Eating healthy eh?")
#     case order:
#         print(f"Enjoy your {order}.")

# class Special:
#     TODAY = 'lasagna'

# lunch_order = input("What do you what for lunch? ").lower().strip()

# match lunch_order:
#     case Special.TODAY:
#         print("Today's special is awesome!")
#     case "taco":
#         print("Taco, taco, TACO, tacotacotaco!")
#     case "salad" | "soup":
#         print("Eating healthy eh?")
#     case order:
#         print(f"Enjoy your {order}.")


class Special:
    TODAY = "lasagna"


lunch_order = input("What do you what for lunch? ").lower().strip()

match lunch_order:
    case Special.TODAY:
        print("Today's special is awesome!")
    case "taco":
        print("Taco, taco, TACO, tacotacotaco!")
    case "salad" | "soup":
        print("Eating healthy eh?")
    case ice_cream if "ice cream" in ice_cream:
        flavour = ice_cream.replace("ice cream", " ").strip()
        print(f"Here's your very grown-up {flavour}...lunch")
    case order:
        print(f"Enjoy your {order}.")
