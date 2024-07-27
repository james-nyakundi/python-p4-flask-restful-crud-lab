from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model, ):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'
