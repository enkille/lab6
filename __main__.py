# Lab 6: Version Control - Group 2
# UF COP3502C Summer 2023
# Encoder: Angelica L Bohl - Copied into cloned repository owned by enkille
# Unable to reach lab partner. My husband created a repository for me to use
# Decoder:


def menu():
    """Menu function for selecting an option"""
    selection = None
    in_menu = True
    while in_menu:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        try:
            selection = int(input('Please enter an option: '))
        except:
            print('Invalid selection!\n')
            continue
        in_menu = False
    return selection


def encode(pw):
    """Function for encoding password"""
    encoded_pw = ''
    for i in pw:
        encoded_pw += str(int(i) + 3)
    return encoded_pw


"""Main body of program for encoding/decoding password"""
encoding = True
password = ''
encoded_pw = ''

while encoding:
    selection = menu()
    if selection == 1:
        password = input('Please enter your password to encode: ')
        encoded_pw = encode(password)
        print('Your password has been encoded and stored!\n')
    elif selection == 2:
        pass
    elif selection == 3:
        break
    else:
        print('Invalid selection!\n')
        continue
