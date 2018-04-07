s_file = open("list_of_songs.csv", "r")

s_file_content = s_file.read()

def menu ():
    choice = input(
    """
    Welcome!!
    Songs to learn - By Rolf Rokseth
        L - List song
        A - Add Song
        C - Mark song complete
        Q - Quit
    """)
    menu_Check(choice)

def menu_Check(choice):
    while choice.upper() not in ['L', 'A', 'C', 'Q']:
        print("Invalid input")
        choice = input(
    """
    Songs to learn - By Rolf Rokseth
        L - List song
        A - Add Song
        C - Mark song complete
        Q - Quit
    """)
    return choice







menu()






print(s_file.name)
print(s_file_content)

s_file.close()