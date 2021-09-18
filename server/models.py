from sqlalchemy import ARRAY, Column, Date, Integer, Text, text

from server import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, server_default=text("nextval('posts_id_seq'::regclass)"))
    rubrics = Column(ARRAY(Text()), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)
