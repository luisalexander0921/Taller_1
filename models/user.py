# models/user.py

class Usuario:
    def __init__(self, id, username, password, es_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin

# Lista de usuarios
usuarios = [
    Usuario(1, 'admin', 'adminpass', es_admin=True),
    Usuario(2, 'user1', 'user1pass'),
    Usuario(3, 'user2', 'user2pass')
]

# Función para obtener un usuario por nombre de usuario
def obtener_usuario_por_username(username):
    for usuario in usuarios:
        if usuario.username == username:
            return usuario
    return None
