from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo'

@app.route('/contato')
def contato():
    return 'alba.lopes@ifrn.edu.br'

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')
    #return '<ul><li>Jailson</li></ul>'

@app.route('/professores')
def professores():
    return render_template('professores.html')



