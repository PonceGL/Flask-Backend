from flask import Flask, jsonify, render_template
from users import users
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "Hello from Python"})

@app.route("/users", methods=["GET"])
def usersHandle():
    return jsonify({"users": users})

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>', methods=["GET"])
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>', methods=["GET"])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>', methods=["GET"])
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    image = "https://flask.palletsprojects.com/en/2.2.x/_static/flask-icon.png"
    return render_template('hello/hello.html', name=name, image=image)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)