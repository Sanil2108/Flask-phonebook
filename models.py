from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contacts'
    cid=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(120))
    phone=db.Column(db.String(10))

    def __init__(self, name, email, phone):
        self.name=name.title()
        self.email=email.title()
        self.phone=phone.title()