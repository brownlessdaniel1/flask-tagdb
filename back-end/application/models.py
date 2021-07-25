from application import db
from sqlalchemy import Table, Column


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    tags = db.relationship(
        'Tag',
        secondary=association,
        lazy='dynamic',
        back_populates='objects'
    )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tkey = db.Column(db.String(30), nullable=False)
    tvalue = db.Column(db.String(30), nullable=False)
    ## Objects = secondary Assoc? - look at other project.
    objects = db.relationship(
        'Object',
        secondary=association,
        lazy='dynamic',
        back_populates='tags'
    )

association = db.Table('association', db.Model.metadata,
    db.Column('id',db.Integer,primary_key=True),
    db.Column('object_id', db.Integer, db.ForeignKey('object.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)
