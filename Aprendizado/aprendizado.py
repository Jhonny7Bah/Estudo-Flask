#Chamando o framework
from flask import Flask

#iniciando o flask a partir do módulo atual '__name__'
app = Flask(__name__)

#agora vamos criar rotas. Rotas são as subpáginas que estão dentro da página.
#é tipo quando você entra em um site, clica em um botão e abre um mesmo conteúdo da mesma página. ALi seria uma outra rota.
#para isso, vamos fazer uso de um decorator, apontando a aplicação e posteriormente, passando sua rota e separando com barra.
@app.route('/') #quando passamos apenas uma barra, siginifica que esta será a rota inicial (quando digitar a url direta)
def principal(): #agora vamos ter que criar uma função que seja correspondente a página
    return '<h2>Olá mundo!! </h2>' #aqui eu passo a tag html e também oq ela fazer na página

app.run() # e com o run eu executo a aplicação.