from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

import secrets
import cs304dbi as dbi
import methods

#This is our starter page
@app.route('/')
def index():
    return render_template('main.html', page_title='Main Page')

@app.route('/nm/<nm>')
def person_lookup(nm):
    nm_num=int(nm)
    conn=dbi.connect()
    person=methods.person_lookup(conn,nm_num)
    return render_template('people.html', 
                            name=person["name"],
                            addedby=person["s.name"],
                            birthdate=person["birthdate"]
                            )

@app.route('/tt/<tt>')
def movie_lookup(tt):
    tt_num=int(tt)
    conn=dbi.connect()
    movie=methods.movie_lookup(conn,tt_num)
    cast=methods.cast_lookup(conn,tt_num)
    return render_template('movie.html', 
                            title=movie["title"],
                            release=movie["release"],
                            cast=cast
                            )



if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    dbi.conf("wmdb")
    app.debug = True
    app.run('0.0.0.0',port)
