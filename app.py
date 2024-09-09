#pip install flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flask-Script
#pip install pymysql
#flask db init
#flask db migrate "Migração Inicial"
#flask db upgrade

from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Cursos
app.config['SECRET_KEY'] = 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'

# drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/CRUD com Flask"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<ano>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'Informático', curso = 'Informática', ano = 2):
    dados = {'nome': nome, 'curso': curso, 'ano': ano}
    return render_template('aula.html', dados_curso = dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados',methods=['POST'])
def dados():
    flash('Dados enviados!!!')
    dados = request.form
    return render_template('dados.html', dados=dados)

@app.route('/cursos')
def cursos():
    u = Cursos.query.all()
    return render_template('cursos_lista.html', dados = u)

@app.route('/cursos/add')
def cursos_add():
    return render_template('cursos_add.html')

@app.route('/cursos/save', methods=['POST'])
def cursos_save():
    nome = request.form.get('nome')
    duracao_horas = request.form.get('duracao_horas')
    custo = request.form.get('custo')
    if nome and duracao_horas and custo:
        cursos = Cursos(nome, duracao_horas, custo)
        db.session.add(cursos)
        db.session.commit()
        flash('Curso cadastrado com sucesso!!!')
        return redirect('/cursos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/cursos/add')
    
@app.route('/cursos/remove/<int:id_curso>')
def cursos_remove(id_curso):
    cursos = Cursos.query.get(id_curso)
    if id_curso > 0:
        db.session.delete(cursos)
        db.session.commit()
        flash('Curso removido com sucesso!!!')
        return redirect('/cursos')
    else:
        flash('Caminho incorreto!!!')
        return redirect('/cursos')

@app.route('/cursos/edita/<int:id_curso>')
def cursos_edita(id_curso):
    cursos = Cursos.query.get(id_curso)
    return render_template('cursos_edita.html', dados = cursos)

@app.route('/cursos/editasave', methods=['POST'])
def cursos_editasave():
    nome = request.form.get('nome')
    duracao_horas = request.form.get('duracao_horas')
    custo = request.form.get('custo')
    id_curso = request.form.get('id_curso')
    if id_curso and nome and duracao_horas and custo:
        cursos = Cursos.query.get('id_curso')
        cursos.nome = nome
        cursos.duracao_horas = duracao_horas
        cursos.custo = custo
        db.session.commit()
        flash('Dados atualizados com sucesso!!!')
        return redirect('/cursos')
    else: 
        flash('Faltando dados!!!')
        return redirect('/cursos')

if __name__ == '__main__':
    app.run()

#Passo a passo para inicializar
    #instalar o python
    #ctrl shift p envirome..
    #verificar se tem o (.venv) no começo do terminal
    #pip install flask
    #flask run --debug