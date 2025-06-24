#importo o flask
from flask import Flask, render_template
#importo também o render_template, que é um adicional do flask que tem como intuito carregar arquivos html.
#é importante constar que na mesma raiz do módulo __main__, é necessário criar uma pasta denominada de templates e colocar dentro dessa pasta todos os html

#inicializo o flask com o módulo atual
app = Flask(__name__)

@app.route('/')
def homepage():
    #para retornar um html, basta eu mandar ele retornar o render_template e informar o nome do arquivo
    return render_template('homepage.html') 

#e se eu quiser passar uma variável para o html?
@app.route('/<usuario>') #dentro do decorator, você coloca a variável dentro de maior e menor <>
#depois passa a variavel como parâmetro para a função
def perfil(usuario):
    #e na chamada do html, coloca o parâmetro usuário da função e também coloca como valor padrão o próprio parâmetro.
    #como vai funcionar? o usuário vai digitar a / e posteriormente, vai informar o valor. 
    #logo, para fazer uso do valor da variável, basta colocar {{nome_da_variavel}} no próprio html
    return render_template('perfil.html', usuario=usuario)  

@app.route('/rota_usuario/<usuario>')
def Perfil_Usuario(rota_usuario):
    from flask import url_for
    #para direcionar o usuário para uma subpasta do site, foi visto que pode ser feito através do endereço da rota, correto?
    # No entanto, caso o endereço acabe mudando, o código quebra. O endereço pode mudar ao decorrer do tempo, mas a função, não.
    # o url_for vai fazer com que seja possível reconhecer uma função python como um endereço de rota
    # e lá no html (na tag a, nesse caso) basta colocar {{url_for('nome_da_funcao')}}
    return render_template('perfil', rota_usuario=rota_usuario)

@app.route('/inicio/noticias')
def noticias():
    return render_template('noticia.html')

app.run()        