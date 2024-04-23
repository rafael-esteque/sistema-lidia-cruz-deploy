from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date())

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date())
    materia_leciona = db.Column(db.String(50))
    
class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serie = db.Column(db.String(10))
    nome = db.Column(db.String(10))
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    usuario_criacao = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(500))
    nome = db.Column(db.String(150))
    sobrenome = db.Column(db.String(150))
    tipo_usuario = db.Column(db.String(150))
    tipo_acesso = db.Column(db.String(150))
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    usuario_criacao = db.Column(db.Integer, db.ForeignKey('usuario.id'))
