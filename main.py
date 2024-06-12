import sqlite3

conn = sqlite3.connect('1.2.db')

cursor = conn.cursor()

print("""
     ______  _______           _____     ____      ____  ____      ______              ______  _______        ______  _____   ______    ____   ____ 
    |      \/       \     ____|\    \   |    |    |    ||    | ___|\     \            |      \/       \   ___|\     \|\    \ |\     \  |    | |    |
   /          /\     \   /     /\    \  |    |    |    ||    ||     \     \          /          /\     \ |     \     \\\    \| \     \ |    | |    |
  /     /\   / /\     | /     /  \    \ |    |    |    ||    ||     ,_____/|        /     /\   / /\     ||     ,_____/|\|    \  \     ||    | |    |
 /     /\ \_/ / /    /||     |    |    ||    |    |    ||    ||     \--'\_|/       /     /\ \_/ / /    /||     \--'\_|/ |     \  |    ||    | |    |
|     |  \|_|/ /    / ||     |    |    ||    |    |    ||    ||     /___/|        |     |  \|_|/ /    / ||     /___/|   |      \ |    ||    | |    |
|     |       |    |  ||\     \  /    /||\    \  /    /||    ||     \____|\       |     |       |    |  ||     \____|\  |    |\ \|    ||    | |    |
|\____\       |____|  /| \_____\/____/ || \ ___\/___ / ||____||____ '     /|      |\____\       |____|  /|____ '     /| |____||\_____/||\___\_|____|
| |    |      |    | /  \ |    ||    | / \ |   ||   | / |    ||    /_____/ |      | |    |      |    | / |    /_____/ | |    |/ \|   ||| |    |    |
 \|____|      |____|/    \|____||____|/   \|___||___|/  |____||____|     | /       \|____|      |____|/  |____|     | / |____|   |___|/ \|____|____|
    \(          )/          \(    )/        \(    )/      \(    \( |_____|/           \(          )/       \( |_____|/    \(       )/      \(   )/  
     '          '            '    '          '    '        '     '    )/               '          '         '    )/        '       '        '   '   
                                                                      '                                          '   """)
# this line makes a function
def get_all_information ():
   
   
   # this line
    cursor.execute('SELECT * FROM Movies;')

#this line fetches the information from the sql database
    Movies = cursor.fetchall()
   
 #no clue what what this does i found this on a cheat sheet on google classroom
    print(f"{'MOVIE NAME':<20}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    for movie in Movies:
        print(f"{movie[1]:<20}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")

def view_all_mystery_movies():
    
    #this line assigns a SQL query string to the variable query
    query = "SELECT * FROM Movies WHERE genre = 'mystery'"
    cursor.execute(query)
   #This line retrieves all the rows returned by the SQL query adn stores it in the variable mystery_movies
    mystery_movies = cursor.fetchall()
    print(f"{'MOVIE NAME':<24}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    for movie in mystery_movies:
        print(f"{movie[1]:<24}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")



def view_all_horror_movies():
    query = "SELECT * FROM Movies WHERE genre = 'horror'"
    #execute the SQL query using the cursor
    cursor.execute(query)
    # Fetch all the results returned by the SQL query
    horror_movies = cursor.fetchall()
    # Print the header row with column names, and i customised the width and position of the text to make it more neat
    print(f"{'MOVIE NAME':<24}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    # loops over each movie in the horror_movies list
    for movie in horror_movies:
    # Print details of each movie 
        print(f"{movie[1]:<24}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")

def view_all_action_movies ():
    query = "SELECT * FROM Movies WHERE genre = 'action'"
    cursor.execute(query)
    action_movies = cursor.fetchall()
    print(f"{'MOVIE NAME':<24}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    for movie in action_movies:
        print(f"{movie[1]:<24}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")
    

def view_all_adventure_movies ():
    query = "SELECT * FROM Movies WHERE genre = 'adventure'"
    cursor.execute(query)
    adventure_movies = cursor.fetchall()
    print(f"{'MOVIE NAME':<24}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    for movie in adventure_movies:
        print(f"{movie[1]:<24}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")


def view_all_comedy_movies():
    query = "SELECT * FROM Movies WHERE genre = 'comedy'"
    cursor.execute(query)
    comedy_movies = cursor.fetchall()
    print(f"{'MOVIE NAME':<24}{'RATING':<10}{'MINUTES':<10}{'GENRE':<14}{'COST$(MILLIONS)':<20}{'EARNED$(MILLIONS)':<20}{'RELEASE DATE':<15}")
    for movie in comedy_movies:
        print(f"{movie[1]:<24}{movie[2]:<10}{movie[3]:<10}{movie[4]:<14}{movie[5]:<20}{movie[6]:<20}{movie[7]:<15}")

    





while True:
    choice = input("\n1. Get all information\n2. Every mystery movie\n3. Every horror movie\n4. Every action movie\n5. Every adventure movie\n6. Every comedy movie\n7. EXIT\n>    ")
    if choice == '1':
        get_all_information()
    elif choice == '2':
        view_all_mystery_movies ()
    elif choice == '3':
        view_all_horror_movies()
    elif choice == '4':
        view_all_action_movies()
    elif choice == '5':
        view_all_adventure_movies()
    elif choice == '6':
        view_all_comedy_movies()
    elif choice == '7':
        print("Thank you for using my program 🥳")
        break
    else:
        print("Invalid Choice")
