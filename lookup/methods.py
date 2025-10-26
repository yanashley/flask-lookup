#By Ruth Perjuste, Sophie Lin, Ashley Yang 

import cs304dbi as dbi 


def person_lookup(conn,nm):
    """Grabs the persons information such as date of birth and who added them to the database and all the 
    movies they have been apart of """
    print(f"This is nm {nm}")
    #if conn is None:
    curs = dbi.dict_cursor(conn)
    curs.execute('''
        select nm, name,birthdate,addedby 
        from person where nm= %s''',
        [nm])
    
    return curs.fetchall()


if __name__ == '__main__':
    conn = get_connection()
    pl = person_lookup(conn,123)
    for person in pl:
        print('{name} born on {date} nm is {nm}, and added by {addedby}'
              .format(name=person['name'],
                      date=person['birthdate'],
                      nm=person["nm"],
                      addedby=person['addedby']))