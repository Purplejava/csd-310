Lidia Goris
4/25/2023
Assignment 8 Movies Update and Delete




def show_films(cursor, title):
    # method to execute an inner joint on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN 
                   genre ON film.genre_id=genre_id INNER JOIN studio ON film.studio-id=studio.studio.studio_id")
    
    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- () --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print ("Film Name; ()\nDirector: ()\nGenre Name ID: ()\nStudio Name: ()\n.format(film(0), film(1), film(2), film(3))")