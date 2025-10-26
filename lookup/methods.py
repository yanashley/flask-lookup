#By Ruth Perjuste, Sophie Lin, Ashley Yang 

import cs304dbi as dbi 


def person_lookup(conn,nm):
    """Grabs the persons information such as date of birth and who added them to the database and all the 
    movies they have been apart of """
    print(f"This is nm {nm}")
    #if conn is None:
    curs = dbi.dict_cursor(conn)
    curs.execute('''
        select nm, p.name,birthdate,addedby, s.name
        from person p
        join staff s on p.addedby=s.uid
        where nm= %s''',
        [nm])
    
    return curs.fetchone()

def discography_lookup(conn,nm):
    """Grabs the movies information such as title release date and more information about the movie"""
    # print(f"This is tt {tt}")
    #if conn is None:
    curs = dbi.dict_cursor(conn)
    curs.execute('''
        select nm, m.tt, m.title
        from credit c
        join movie m on c.tt=m.tt
        where nm= %s''',
        [nm])
    
    return curs.fetchall()

def movie_lookup(conn,tt):
    """Grabs the movies information such as title release date and more information about the movie"""
    print(f"This is tt {tt}")
    #if conn is None:
    curs = dbi.dict_cursor(conn)
    curs.execute('''
        select tt, title, `release`
        from movie
        where tt= %s''',
        [tt])
    
    return curs.fetchone()

def cast_lookup(conn,tt):
    """Grabs the movies information such as title release date and more information about the movie"""
    print(f"This is tt {tt}")
    #if conn is None:
    curs = dbi.dict_cursor(conn)
    curs.execute('''
        select tt, p.nm, p.name
        from credit c
        join person p on p.nm=c.nm
        where tt= %s''',
        [tt])
    
    return curs.fetchall()

def form_lookup(conn, query, kind):
    '''Return list of actors or movies that match the search query'''
    curs = dbi.dict_cursor(conn)
    if kind == 'movie_title':
        pattern = '%'+query + '%'
        curs.execute('''
        select tt, title from movie
        where title like %s''',
        [pattern])
    else:
        pattern = '%'+query + '%'
        curs.execute('''
        select nm, name from person
        where name like %s''',
        [pattern])
    return curs.fetchall()
    

    
if __name__ == '__main__':
    dbi.conf("wmdb")
    conn=dbi.connect()
    movie = movie_lookup(conn,int(1454468))
    print('{title} born on {release} '
            .format(title=movie['title'],
                    release=movie['release']))

    
    #print('{name} born on {date} nm is {nm}, and added by {addedby}'
            #.format(name=person['name'],
                    #date=person['birthdate'],
                    #nm=person["nm"],
                    #addedby=person['addedby']))
