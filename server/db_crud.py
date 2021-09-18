from sqlalchemy.orm import Session

import models

from elastic import Elastic

elastic = Elastic()


def delete_post_by_id(db: Session, id: int):
    deleted_post = elastic.search_by_id(id)

    if deleted_post is not None:
        elastic_deleted = elastic.delete_by_id(deleted_post[0]['_id'])

        db_deleted = bool(db.query(models.Post).filter(models.Post.id == id).delete())

        db.commit()

        return all((elastic_deleted, db_deleted))
    return False

def get_posts(db: Session, text:str):



d
