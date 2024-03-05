from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo'

@app.route('/contato')
def contato():
    telefone = '1234-5678'
    email = 'alba.lopes@ifrn.edu.br'
    return render_template('contato.html', x = email, tel = telefone)
    

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')
    #return '<ul><li>Jailson</li></ul>'

@app.route('/professores')
def professores():
    return render_template('professores.html')

'''
@app.route('/usuario')
@app.route('/usuario/<nome>')
def usuario(nome='anônimo'):
    return render_template('usuario.html', nome=nome)
'''

@app.route('/usuario', defaults={"nome": "anônimo"})
@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

@app.route('/dobro', defaults={"n": 1})
@app.route('/dobro/<int:n>')
def dobro(n):
    calculo = 2*n
    return 'O dobro é: '+str(calculo)

@app.route('/soma', defaults={'n1': 0, 'n2': 0})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    result = n1 + n2
    return render_template('soma.html', a=n1, b=n2, c=result)
