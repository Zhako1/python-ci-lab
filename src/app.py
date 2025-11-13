from flask import Flask, jsonify
from main import add, is_palindrome

app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify({"result": add(a, b)})

@app.route("/palindrome/<string:s>")
def palindrome_route(s):
    return jsonify({"result": is_palindrome(s)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
