from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/news/<id>")
def news_by_id(id):
    return 'Hi: ' + id


if __name__ == "__main__":
    app.run(port=5010, debug=True)
