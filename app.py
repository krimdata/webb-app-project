from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, les amis ! bienvenue dans notre web app."

if __name__ == "__main__":
    app.run(debug=True)
