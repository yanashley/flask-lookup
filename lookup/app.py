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
    return render_template('main.html', page_title='Main Page')


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
