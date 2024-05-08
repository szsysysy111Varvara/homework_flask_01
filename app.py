from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return f"Hello, Flask!"

@app.route('/user/<user_name>')
def get_greeting_user(user_name):
    return f"Hello, {user_name}!!!"

if __name__ == '__main__':
    app.run(debug=True)