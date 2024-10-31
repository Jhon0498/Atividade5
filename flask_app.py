from flask import Flask, request, render_template
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)

moment = Moment(app)

@app.route('/')
def hello_world():
    name = "eu estou usando o JINJA2!"
    return render_template('template-base.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def hello_pront(name):
    return render_template('user.html', name=name, pront='PT3026931', ins='IFSP', current_time=datetime.utcnow())

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', current_time=datetime.utcnow()), 404

@app.route('/contextorequisicao')
def hello_requisi_detalhes():
    navegador = request.headers.get('User-Agent')
    Ip_remoto = request.headers.get('X-Forwarded-For')
    host_name = request.headers.get('Host')
    return render_template('contextorequisicao.html', name='Jhonatan', navegador=navegador, IP_cliente=Ip_remoto, host_name=host_name)


if __name__ == '__main__':
    app.run(debug=True)
