from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
import os
from .models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)



@auth.route("/", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email_input')
        password = request.form.get('password_input')
        
        user = Usuario.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.senha, password):
                flash('Logado com sucesso', category='success')
                login_user(user, remember=True)
                print(current_user.email)
                return redirect(url_for('views.home'))
            else:
                flash('Usuário ou senha incorretos', category='error')
        else:
            flash('Este usuário não está cadastrado', category='error')
    
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Deslogado com sucesso', category='success')
    return redirect(url_for('auth.login'))

@auth.route("/request-acess")
def request_acess():
    return render_template("request-acess.html")


@auth.route("/create-acess", methods=["GET", "POST"])
@login_required
def create_acess():
    if request.method == "POST":
        email = request.form.get("input_email")
        name = request.form.get("input_name")
        surname = request.form.get("input_surname")
        password01 = request.form.get("input_password01")
        password02 = request.form.get("input_password02")
        user_type = request.form.get("input_user_type")
        user_acess_type = request.form.get("input_acess_type")
        confirmation_check = request.form.get("confirmation_check")

        
        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('Email já cadastrado', category='error')
        if len(email) < 4:
            flash('Email deve conter um formato válido', category='error')
        elif password01 != password02:
            flash('As senhas não são iguais', category='error')
        elif len(password01) < 7:
            flash('A senha deve ter pelo menos 7 caracteres', category='error')
        elif len(name) < 2:
            flash('O primeiro nome deve ter mais do que um caractere', category='error')
        elif len(surname) < 2:
            flash('O sobrenome deve ter mais do que um caractere', category='error')
        elif user_type is None:
            flash('O Tipo de Usuário deve ser especificado', category='error')
        elif user_acess_type is None:
            flash('O Tipo de Acesso deve ser especificado', category='error')
        elif confirmation_check == False:
            flash('Necessário confirmar a criação da conta', category='error')
        else:
           new_user = Usuario(email=email, senha=generate_password_hash(
               password01)
                              , nome=name
                              , sobrenome=surname
                              , tipo_usuario=user_type
                              , tipo_acesso=user_acess_type
                              , usuario_criacao=1)
           db.session.add(new_user)
           db.session.commit()
           flash('Conta criada com sucesso', category='success')
           return redirect(url_for('views.home'))
        
    
    return render_template("create-acess.html")
