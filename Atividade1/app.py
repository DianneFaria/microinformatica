from flask import Flask, render_template, request, url_for

from flask_mysqldb import MySQL

app = Flask(__name__)


# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'dianne'
app.config['MYSQL_PASSWORD'] = 'Sintaavibe123**'
app.config['MYSQL_DB'] = 'desafio4'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

'''
@app.route("/contato")
def contato():
    return render_template("contato.html")
'''

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))


        mysql.connection.commit()


        cur.close()

        return'sucesso'
    return render_template('contato.html')


#rota usuários para listar todos os usuários no banco de dados
@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)
