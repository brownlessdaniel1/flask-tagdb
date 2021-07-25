from app import db
from application.models import Object, Tag


def asdf():

    db.drop_all()
    db.create_all()

    apple = Object(name="apple")
    t1 = Tag(tkey="colour",tvalue="red")
    t2 = Tag(tkey="shape", tvalue="round")
    db.session.add(apple)
    db.session.add(t1)
    db.session.add(t2)
    apple.tags.append(t1)
    apple.tags.append(t2)
    db.session.commit()

def read():
    print([{tag.tkey: tag.tvalue}for tag in Object.query.first().tags])
    print([item.tkey for item in Tag.query.all()])
    print([item.tvalue for item in Tag.query.all()])

read()
# asdf()