from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Running"


@app.route('/sum_of_two/<int:a>/<int:b>')
def sum(a, b):
    d = {'first number': a, 'second number': b, 'sum': a + b}
    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True)
