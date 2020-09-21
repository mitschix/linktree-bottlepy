#!/usr/bin/env python
from userdata import USER_INFO
import os

working_dir = os.path.dirname(os.path.realpath(__file__))
activate_this = os.path.join(working_dir, "venv_bottle/bin/activate_this.py")
exec(open(activate_this).read(), {'__file__': activate_this})

from bottle import route, run, template, request, static_file, default_app, redirect

def get_token():
    with open("token_file", 'r') as rf:
        ret_token = rf.readline().strip()
    return ret_token


@ route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')


@ route('/links')
def linktree():
    token = request.query.get('at')
    cur_token = get_token()
    print(cur_token)
    if token == cur_token:
        name = USER_INFO.get("name")
        sname = USER_INFO.get("sname")
        github = USER_INFO.get("github")
        ig = USER_INFO.get("ig")
        email = USER_INFO.get("email")
        fb = USER_INFO.get("fb")
        twitter = USER_INFO.get("twitter")
        reddit = USER_INFO.get("reddit")
        youtube = USER_INFO.get("youtube")

        return template('linktree', name=name, ig=ig, github=github, email=email,
                        sname=sname, facebook=fb, twitter=twitter, reddit=reddit,
                        youtube=youtube)
    else:
        redirect('/')


@ route('/')
def index():
    return template('index')


application = default_app()

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, reloader=True)
