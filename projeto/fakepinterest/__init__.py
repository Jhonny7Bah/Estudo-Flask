from flask import Flask #type:ignore
from flask_sqlalchemy import SQLAlchemy #type:ignore #importante para banco de dados


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database = SQLAlchemy(app)

##criação de banco de dados (executar a função quando quiser criar um)
def criar_banco_de_dados():
    with app.app_context():
        database.create_all()


from fakepinterest import routes