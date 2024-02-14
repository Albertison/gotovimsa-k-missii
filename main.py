from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def requi():
    params = {}
    params['title'] = 'Загатовка'
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')