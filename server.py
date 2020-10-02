from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return "Hi!"


@app.route("/news/<id>")
def news_by_id(id):
    return 'Hi: ' + id


if __name__ == "__main__":
    app.run(port=5010, debug=True)
