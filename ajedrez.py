from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def ajedrez():
    return render_template('index.html')


@app.route('/<int:num>')
def ajedrez2(num):
    numero = int(num / 2)
    return render_template('index2.html',numero=numero)


@app.route('/<int:num>/<int:num2>')
def ajedrez3(num,num2):
    numero = int(num / 2)
    numero2 = int(num2 /2)
    return render_template('index3.html',numero=numero,numero2=numero2)


@app.route('/<int:num>/<int:num2>/<string:col1>/<string:col2>')
def ajedrez4(num,num2,col1,col2):
    estilo1= f'style=background-color:{col1}'
    estilo2= f'style=background-color:{col2}'
    numero = int(num / 2)
    numero2 = int(num2 /2)
    return render_template('index4.html',numero=numero,numero2=numero2,estilo1=estilo1,estilo2=estilo2)


if __name__=='__main__':
    app.run(debug=True)