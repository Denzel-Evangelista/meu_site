from flask import Flask, render_template

app = Flask(__name__)

#TODA A PAGINA SEMPRE TEM UM ROUTE E UMA FUNÇÃO
#route >> caminho depois do dominio
#função >> o que você quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contato")
def contatos():
    return render_template("contatos.html")

@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario) 

if __name__ == "__main__":
    app.run(debug=True) #coloca o site no ar