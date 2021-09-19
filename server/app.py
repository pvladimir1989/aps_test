from flask import Flask, request

from sqlalchemy.orm import Session


from server import db_crud
from server.database_settings import SessionLocal


app = Flask(__name__)


# Коннект с СУБД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.route("/get_posts", methods=["GET"])
def get_posts(db: Session = get_db):
    try:
        query = request.args["query"]
        results_posts_list = db_crud.get_posts(db=db, text=query)
        return {"result": results_posts_list}
    except Exception as exc:
        return str(exc)


@app.route("/delete_post", methods=["DELETE"])
def delete_post(db: Session = get_db):
    try:
        id_for_delete = int(request.args["id"])
        result_delete = db_crud.delete_post_by_id(db=db, id_delete=id_for_delete)
        return {'result_delete': result_delete}
    except Exception as exc:
        return str(exc)


if __name__ == '__main__':
    app.run()
