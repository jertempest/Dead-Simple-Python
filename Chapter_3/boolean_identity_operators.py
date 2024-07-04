spam = True
eggs = False
potatoes = None

if spam is True:
    print("We have spam.")
if spam is not True:
    print("I don't like spam!").upper()

if spam:
    print("Spam, spam, spam, spam...")

if eggs is False:
    print("We are out of eggs.")
if eggs is not True:
    print("No eggs, but we have spam, spam, spam, spam...")
if not eggs:
    print("Would you like spam instead?")

if potatoes is not None:
    print("Yum")
if potatoes is None:
    print("Yes, we have potatoes.")

if eggs is spam:
    print("This won't work.")
    