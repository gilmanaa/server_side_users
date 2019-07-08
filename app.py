from bottle import route, run, template, static_file, request
import os
import json

users = ["gilmanaa","nickyc","cefi"]
addError = {"msg":"User exists"}
addSuccess = {"msg":"User added"}
delError = {"msg":"User doesn't exist"}
delSuccess = {"msg":"User deleted"}

@route('/getUsers')
def get_users():
    return json.dumps(sorted(users))

@route('/addUser', method="POST")
def add_user():
    new_user = request.POST.get("user")
    if new_user == "":
        return json.dumps(addError)
    for user in users:
        if new_user == user:
            return json.dumps(addError)
    users.append(new_user)
    return json.dumps(addSuccess)

@route('/delUser', method="POST")
def del_user():
    delete_user = request.POST.get("user")
    for user in users:
        if delete_user == user:
            users.remove(delete_user)
            return json.dumps(delSuccess)
    return json.dumps(delError)

@route('/')
def index():
    return template(os.path.dirname(__file__) + "/index.html")

@route('/<filename:re:.*\.css>')
def styles(filename):
    return static_file(filename,root="")

@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename,root="")

def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()