# Emily Apel

encoder = True
def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit \n"""
)

def encode(password):
    final_pass = ""
    for dig in user_pass:
        d = int(dig)
        if (d + 3) > 9:
            d = (d + 3) % 10
        else:
            d = d + 3
        final_pass += str(d)

    return final_pass


def decoder(encoded_pass):
    pass

user_pass = None
encoded_pass = None
while encoder:
    menu()
    choice = int(input("Please enter an option: "))

    if choice == 1:
        user_pass = input("Please enter your password to encode: ")
        encoded_pass = encode(user_pass)
        print("Your password has been encoded and stored!")

    elif choice == 2:
        pass
    elif choice == 3:
        break