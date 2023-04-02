from flask import Flask, render_template, request, session, redirect, jsonify
import json
from typing import TypedDict
import dbManager as dbm
app = Flask(__name__)

app.secret_key = "BqzK4uMKPH"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['POST', 'GET']) #change to login later on
def login():
    error = None
    if request.method == 'POST':
        print('Running Post')
        uid = request.form['uid']
        password = request.form['password']
        if dbm.is_valid_password(uid,password):
            session['uid'] = uid
            print('correct entered')
            return redirect('/profile')
        else:
            print('Retry')
            return render_template('login.html', error=error, msg="Entered username or password is incorrect. Try again!")
    return render_template('login.html')
@app.route('/create_user',methods=['POST', 'GET'])
def create_user():
    error = None
    if request.method == 'POST':
        print('Running Post')
        uid = request.form['uid']
        password = request.form['password']
        name = request.form['name']
        msg=""
        if len(uid)<4:
            #Not a valid uid was entered
            msg = "Username provided is too short, make the username longer than 4"
        elif dbm.is_user(uid):
            msg = "Account with this uid already exist"
        elif password == "" :
            #No password was entered
            msg = "No password was entered, try again!"
        elif len(password)<7:
            #Password too short
            msg = "Password is too short, has to be at least 7 characters"
        elif len(name)<2:
            msg = "No name was entered, try again!"
        else:
            dbm.insert_user(name,uid, password)
            return redirect('/login')
        return render_template('create_user.html', error=error, msg=msg)
    return render_template('create_user.html')
#Static Routes'''
'''
@app.route('/common.css')
def common():
    return render_template('/common.css')
@app.route('/index.css')
def indexcss():
    return render_template('/index.css')
@app.route('/index.js')
def indexjs():
    return render_template('/index.js')'''

@app.route('/forum/<string:topic>')
def forum(topic: str):
    request = dbm.get_posts(topic)
    return render_template('forum.html', topic=topic, result=request)

@app.route('/forumleftrep/<string:pid>')
def forumleftrep(pid: str):
    values = dbm.get_postRep(pid)
    return render_template('forumleftrep.html', result=values)

@app.route('/forumrightrep/<string:pid>')
def forumrightrep(pid: str):
    primarytext = dbm.get_post(pid)
    values = dbm.get_postRep(pid)
    return render_template('forumrightrep.html', result=values, primarytext=primarytext)

@app.route('/addpost')
def addpost():
    if "topic" not in request.args:
        return ("Missing topic", 404)

    topic = request.args.get('topic')
    reply_target_pid = (request.args.get('reply_target_pid')
            if 'reply_target_pid' in request.args else '')
    return render_template('add_post.html', topic=topic, reply_target_pid=reply_target_pid)


class AddPostBody(TypedDict):
    title: str
    body: str
    topic: str

@app.route('/api/post', methods=['POST']) 
def record_post():
    body: AddPostBody = json.loads(request.data)

    uid = 0 # placeholder uid
    # dbm.insert_post()
    
    return jsonify(
        new_post_id=0, # placeholder pid
    )


if __name__ == '__main__':
    app.run()
