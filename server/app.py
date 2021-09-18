from flask import Flask

app = Flask(__name__)


@app.route("/get_posts", methods=["GET"])
def get_posts():  # put application's code here
    return 'Hello World!'

@app.route("/delete_post", methods=["DELETE"])
def delete_post():
    result_delete=db.delete_post_by_id()

    return result






if __name__ == '__main__':
    app.run()
