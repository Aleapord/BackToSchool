from exts import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Stringr(32), nullable=False)
    gender = db.Column(db.String(4), nullable=False)
    student_card = db.Column(db.String(32), nullable=False)
    college = db.Column(db.String(32), nullable=False)
    classes = db.Column(db.String(32), nullable=False)
    identity_card = db.Column(db.String(32), nullable=False)
    bank_card = db.Column(db.String(19), nullable=False)
    qq = db.Column(db.String(16))
    phone = db.Column(db.String(11))
    mail = db.Column(db.String(320))
    origin = db.Column(db.String(32))
    school = db.Column(db.String(32))
    verified = db.Column(db.SmallInteger, nullable=False)


class Classes(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    college_id = db.Column(db.Integer,db.ForeignKey('college.id'))
    college = db.relationship('College',)

class College(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
