from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class cadTime:
    def __init__(self, nome, jogo, players, ranking):
        self.nome = nome
        self.jogo = jogo
        self.players = players
        self.ranking = ranking
lista = []

@app.route('/')
def main():  # put application's code here
    return render_template('main.html', listaTimes=lista)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/criar', methods=['POST']) #Rota intermediaria
def criar():
    time = request.form['time']
    jogo = request.form['jogo']
    players = request.form['players']
    ranking = request.form['ranking']
    novo = cadTime(time, jogo, players, ranking)
    lista.append(novo)
    return redirect('/')

if __name__ == '__main__':
    app.run()
