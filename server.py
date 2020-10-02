from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi!"

app.route("/news/<news_id>")
def news_by_id(news_id):
    return 'Новость: ' + news_id

if __name__ == "__main__":
    app.run(port=5010, debug=True)
