import csv

def start():
    print("Welcome to <Songs to Learn> - By Rolf Rokseth")
    menu()

def menu ():
    choice: str = input(
    """
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
        choice: str = input(
    """
    Songs to learn - By Rolf Rokseth
        L - List song
        A - Add Song
        C - Mark song complete
        Q - Quit
    """)
    menu_Choice(choice.upper())

# TODO Add whole menu
def menu_Choice(choice):
    if choice == "L":
        list_Songs()
    elif choice == "Q":
        quit()
    elif choice == "A":
        line_Input()

# TODO Show learned songs
# TODO Number songs
def list_Songs():
    with open('list_of_songs.csv', 'r') as f:
        csv_reader = csv.reader(f)

        next(csv_reader)

        for line in csv_reader:
            print(line)
    menu()

# TODO Handle the input.
# TODO No path after.
def line_Input():
    songloop = 1
    while songloop > 0:
        new_Song = str(input("Song: "))
        if len(new_Song) > 20 or len(new_Song) < 3:
            print("Please keep the song title between 3 and 20 characters")
        else:
            print("Song title saved to file")
            songloop = 0

    artistloop = 1
    while artistloop > 0:
        new_Artist = str(input("Artist: "))
        if len(new_Artist) > 20 or len(new_Artist) < 3:
            print("Please keep the artist name between 3 and 20 characters")
        else:
            print("Artist name saved to file")
            artistloop = 0

    yearloop = 1
    while yearloop > 0:
        new_Year = str(input("Year: "))
        if len(new_Year) == 4 and str.isnumeric(new_Year) == True:
            print("Year saved to file")
            yearloop = 0
        else:
            print("Please enter the year of song release in YYYY format")




def add_Song():
    with open('list_of_songs.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)

        thewriter.writerow(['col1','col2','col3','col4'])



        for line in csv_reader:
            print(line)
    menu()


def quit():
    print("Exiting program")

start()