from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    population = db.Column(db.Integer, nullable=True)
    orbital_period  = db.Column(db.Integer, nullable=True)
    rotation_period = db.Column(db.Integer, nullable=True)
    diameter = db.Column(db.Integer, nullable=True)
    # favoritos = db.relationship ('favoritos', backref= 'planets', lazy=True)
    def __repr__(self):
        return '<planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "climate": self.climate,
            "population": self.population, 
            "orbital_period": self.orbital_period,  
            "rotation_period": self.rotation_period,
            "diameter": self.diameter
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    height = db.Column(db.Integer, nullable=True)
    skin_color = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    # favoritos = db.relationship ('favoritos', backref= 'characters', lazy=True)
    def __repr__(self):
        return '<characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "birth_year": self.birth_year,
            "gender": self.gender, 
            "height": self.height,  
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
            # do not serialize the password, its a security breach
        }
    
# class Favorito(db.Model):
#     __tablename__ = 'favoritos'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     characters_id= db.Column(db.Integer, db.ForeignKey('characters.id'),nullable=True)
#     planets_id= db.Column(db.Integer, db.ForeignKey('planets.id'),nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
#                         nullable=False)
#     def to_dict(self):
#         return {}



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    # favoritos = db.relationship ('favoritos', backref= 'users', lazy=True)


    def __repr__(self):
        return '<users %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    