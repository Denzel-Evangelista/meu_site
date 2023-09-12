from flask import Flask, render_template

app = Flask(__name__)

#TODA A PAGINA SEMPRE TEM UM ROUTE E UMA FUNÇÃO
#route >> caminho depois do dominio
#função >> o que você quer exibir naquela página

@app.route("/")
def homepage():
    return render_template("homepage.html") 

if __name__ == "__main__":
    app.run(debug=True) #coloca o site no ar