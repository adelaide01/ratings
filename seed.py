"""
seed.py

"""

import csv
import model
import datetime

""" CSV files are hardcoded, but another option is args. """
#import sys
#script, filename = argv
# filepath = sys.argv
# print filepath
# print "Parsing: %s" % filepath

def load_users(session):
    """ Import file u.user into database. """
    
    with open("seed/u.user") as f:
        reader = csv.reader(f, delimiter = "|")
        for row in reader:
            user = model.User(id=row[0], age=row[1], zipcode=row[4])
            session.add(user)

def load_movies(session):
    """ Import file u.item into database. """
    """ Decode movie title from Latin-1 format to database friendly unicode. """
    """ Make date string into a datetime format of day, month, year. """

    with open("seed/u.item") as f:
        reader = csv.reader(f, delimiter = "|")
        
        for row in reader:
            # Set id = to row 0.
            id = int(row[0])
            # Set movie title = to row 1 and decode from UTF-8 to Latin-1.
            title = row[1].decode("latin-1")
            
            # Format date in %d-%b-%Y or day-month-year or 00-00-0000.
            released_at = row[2]      
            if released_at: # Applies to places where a date exists. Sometimes dates don't exist.
                formatted_date = datetime.datetime.strptime(released_at, "%d-%b-%Y")
            else:
                None # No format for empty date fields.
            
            # Set URL = to row 4.            
            url = row[4]

            movie = model.Movie(id=id, title=title, released_at=formatted_date, url=url)    
            session.add(movie)


def load_ratings(session):
    """ Import file u.data into database."""

    with open("seed/u.data") as f:
        reader = csv.reader(f, delimiter = "\t")

        for row in reader:
            rating = model.Rating(user_id=row[0], movie_id=row[1], rating=row[2])
            session.add(rating)


def main(session):
    """ Call each of the load_* functions with the session as an argument. """
    load_users(session)
    load_movies(session)
    load_ratings(session)
    session.commit()

if __name__ == "__main__":
    s = model.connect()
    main(s)