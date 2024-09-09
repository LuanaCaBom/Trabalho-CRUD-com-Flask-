from database import db

class Cursos(db.Model):
    __tablename__ = "cursos"
    id_curso = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    duracao_horas = db.Column(db.Integer)
    custo = db.Column(db.Float(10,2))
    
    def __init__(self, nome, duracao_horas, custo):
        self.nome = nome
        self.duracao_horas = duracao_horas
        self.custo = custo

    def __repr__(self):
        return "<Curso: {}>".format(self.nome)