from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/task_1')
def task_1():
    return render_template("task_1.html")


if __name__ == '__main__':
    app.run()
