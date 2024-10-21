
from datetime import datetime
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    # Obtem a data e hora atual
    now = datetime.now()
    # Formata a data e hora em uma string
    current_time = now.strftime("%B %d, %Y %I:%M %p")

    # Renderiza o template index.html com a variável current_time
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/identificacao/<nome>/<prontuario>/<instituicao>')
def saudacao(nome, prontuario, instituicao):
    return render_template('identificacao.html', nome=nome, prontuario=prontuario, instituicao=instituicao)


@app.route('/contextorequisicao/<username>')
def contexro(username):
    # Puxando informações do navegador, IP e host
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    host = request.host

    # Renderizando a página com as variáveis
    return render_template('contexto.html', username=username, user_agent=user_agent, ip_address=ip_address, host=host)

if __name__ == "__main__":
    app.run(debug=True)
