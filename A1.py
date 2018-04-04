
def Menu ():
    choice = input(
    """
    Songs to learn - By Rolf Rokseth
        L - List song
        A - Add Song
        C - Mark song complete
        Q - Quit
    """)
    Menu_Check(choice)

def Menu_Check(choice):
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









Menu()
