def start():
    print("\n   Welcome to <Songs to Learn> - By Rolf Rokseth","\n  ",len(songlist),"Songs loaded")


    menu()


def menu():
    choice: str = input(
    """
    Menu:
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
    Menu:
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
        all_songs_learned()


def list_Songs(songlist):
    i = 1
    for row in songlist:
        print('{0}.{4:2}{1:30}-{2:30}({3})'.format(i, row[0], row[1], row[2], row[3]))
        i = i + 1
    songlist_string = str(songlist)
    songlist_count = songlist_string.count('*')
    number_of_songs = len(songlist)
    print("\n", number_of_songs - songlist_count, "Songs learned, ", songlist_count, "songs still to learn")
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
            print(new_Song,"by",new_Artist,"(",new_Year,") Added to song list")
        else:
            print("Please enter the year of song release in YYYY format")
    new_Line = [new_Song, new_Artist, new_Year, '*']
    add_Song(new_Line, songlist)


def add_Song(new_Line, songList):
    songList.append(new_Line)

    menu()
    return songList

def all_songs_learned():
    songstring = str(songlist)
    if songstring.count("*") == 0:
        print("No more songs to learn!")
        menu()
    else:
        complete_song_verify()

def complete_song_verify():
    while True:
        maxchoice = len(songlist)
        try:
            songlist_decision = int(input("Enter the number of the song you want to complete: ")) - 1
            if songlist_decision < 0:
                print("Please dont enter 0 or negative numbers")
                continue
            if songlist_decision > maxchoice:
                print("Please enter a number between 1 and",maxchoice)
                continue
            if songlist[songlist_decision][3] == " ":
                print("You have already learned",songlist[songlist_decision][0])
                menu()
        except ValueError:
            print("Invalid input, please enter a valid number")
            continue
        else:
            print("\n")
            break

    complete_song(songlist_decision)

def complete_song(songlist_decision):

    songlist[songlist_decision] = [songlist[songlist_decision].replace('*', ' ')
                                   for songlist[songlist_decision] in songlist[songlist_decision]]
    print("Congratulations on learning the song:", songlist[songlist_decision][0], "by", songlist[songlist_decision][1])
    menu()


def quit(f, songlist):
    print(len(songlist),"Songs saved to list_of_songs.csv - Exiting program")
    for i in range(0, len(songlist)):
        song_detail = songlist[i]
        if song_detail[3] == "*":
            song_detail[3] = "y"
        else:
            song_detail[3] = "n"
    with open('list_of_songs.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')

        writer.writerows(songlist)


import csv

f = open("list_of_songs.csv", "r")

reader = csv.reader(f)
songlist = list(reader)

for i in range(0, len(songlist)):
    song_detail = songlist[i]
    if song_detail[3] == "y":
        song_detail[3] = "*"
    else:
        song_detail[3] = " "

start()

f.close()