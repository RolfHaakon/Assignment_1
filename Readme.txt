Songs to Learn - by Rolf Rokseth

-Open menu
    L - List song
    A - Add Song
    C - Mark song complete
    Q - Quit


-L
    List song (
    0. Song name - Singer ( Year )
    1. Song name - Singer ( Year )
    2. Song name - Singer ( Year )
    3. Song name - Singer ( Year )
    4. *Song name - Singer ( Year )
    3 Songs learned, 2 Songs left to learn
    * = Still have to learn.

-Open menu
    L - List song
    A - Add Song
    C - Mark song complete
    Q - Quit

-C
"Enter the number of the song to mark as learned"

-A
"Title:"
"Artist:"
"Year:"


start()
stop = 0
while (stop < 1):
    menu()
    if choice == "L":
        list_Songs()
        print("List songs")
    elif choice == "Q":
        quit()



Free Bird,Lynyrd Skynyrd,1973
Redemption song,Bob Marley,1980
Under pressure,Logic,2014
Blood in Blood out,Jedi Mind Tricks,2003
My Way,Frank Sinatra,1969

new_title = input("Enter title")
new_artist = input("Enter artist")
new_year = input("Enter year")
new_song = [new_title, new_artist, new_year]

your_list.append(new_song)