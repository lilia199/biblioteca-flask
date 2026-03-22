from flask_login import UserMixin

# Esta clase le enseña a Flask qué datos tiene un usuario
class Usuario(UserMixin):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

