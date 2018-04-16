import csv

f = open("list_of_songs.csv", "r")


def start():
    print("Welcome to <Songs to Learn> - By Rolf Rokseth")
    menu()


def menu():
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



def menu_Choice(choice):
    if choice == "L":
        list_Songs(songlist)
    elif choice == "Q":
        quit(f, songlist)
    elif choice == "A":
        line_Input()
    elif choice == "C":
        complete_song()



def list_Songs(songlist):
    i = 1
    for row in songlist:
        print('{0}.{4:2}{1:30}-{2:30}({3})'.format(i, row[0], row[1], row[2], row[3]))
        i = i + 1
    menu()
    return songlist



def line_Input():
    songloop = 1
    while songloop > 0:
        new_Song = str(input("Song: "))
        if len(new_Song) > 20 or len(new_Song) < 1:
            print("Please keep the song title between 1 and 20 characters")
        else:
            songloop = 0

    artistloop = 1
    while artistloop > 0:
        new_Artist = str(input("Artist: "))
        if len(new_Artist) > 20 or len(new_Artist) < 1:
            print("Please keep the artist name between 1 and 20 characters")
        else:
            artistloop = 0

    yearloop = 1
    while yearloop > 0:
        new_Year = str(input("Year: "))
        if len(new_Year) == 4 and str.isnumeric(new_Year) == True:
            yearloop = 0
            print("Song added")
        else:
            print("Please enter the year of song release in YYYY format")
    new_Line = [new_Song, new_Artist, new_Year, '*']
    add_Song(new_Line, songlist)


def add_Song(new_Line, songList):
    songList.append(new_Line)

    menu()
    return songList

def complete_song():
    i = 1
    for row in songlist:
        print('{0}.{4:2}{1:30}-{2:30}({3})'.format(i, row[0], row[1], row[2], row[3]))
        i = i + 1
    listlenght = len(songlist)


    songlist_decision = int(input("Enter the number of the song you want to complete"))-1
    songlist[songlist_decision] = [songlist[songlist_decision].replace('*', ' ')
                                   for songlist[songlist_decision] in songlist[songlist_decision]]
    print(songlist[songlist_decision]," learned")
    menu()

def quit(f, songlist):
    print("Exiting program")
    with open('list_of_songs.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')

        writer.writerows(songlist)


reader = csv.reader(f)
songlist = list(reader)

start()

f.close()