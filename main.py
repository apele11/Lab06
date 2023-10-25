encoder = True

def menu():
    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit \n"""
)

def encode():
    user_pass = input("Please enter your password to encode: ")
    final_pass = ""
    for dig in user_pass:
        d = int(dig)
        if (d + 3) > 9:
            d = (d + 3) % 10
        else:
            d = d + 3
        final_pass += str(d)

    print(final_pass)


while encoder:
    menu()
    choice = int(input("Please enter an option: "))
    if choice == 1:
        encode()