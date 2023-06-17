from flask import Flask

app = Flask(__name__)


@app.route('/start')
def hello_world():  # put application's code here
    return 'Hello! Welcome to Kubernetes!'


if __name__ == '__main__':
    app.run(port=8989)
