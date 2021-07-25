from application import db

class Association(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer, db.ForeignKey("object.id"), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    ## Tags = secondary Assoc? - look at other project.

class tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tkey = db.Column(db.String(30), nullable=False)
    tkey = db.Column(db.String(30), nullable=False)
    ## Objects = secondary Assoc? - look at other project.
