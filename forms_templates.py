from flask import Flask, request, render_template, session, url_for, redirect, flash
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave forte'
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual teu nome?', validators=[DataRequired()])
    sobreNome = StringField('Qual teu sobrenome?', validators=[DataRequired()])
    inst = StringField('Informe a sua Instituição de ensino:', validators=[DataRequired()])
    disciplina = SelectField('Informe a sua disciplina',
                             choices=[('DWEBS', 'Desenvolvimento Web: Servidor'),
                                      ('GSTI', 'Gestão de TI'),
                                      ('EX4', 'Projeto de Extensão 4')])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = NameForm()
    if form.validate_on_submit():
        session['navegador'] = request.headers.get('User-Agent')
        session['Ip_remoto'] = request.headers.get('X-Forwarded-For')
        session['host_name'] = request.headers.get('Host')
        session['name'] = form.name.data
        session['sobreNome'] = form.sobreNome.data
        session['inst'] = form.inst.data
        session['disciplina'] = form.disciplina.data
        return redirect(url_for('hello_world'))
    return render_template(
        'formularioTeste.html',
        form=form,
        name=session.get('name'),
        sobreNome=session.get('sobreNome'),
        inst=session.get('inst'),
        disciplina=session.get('disciplina'),
        browser=session.get('navegador'),
        ip_remoto=session.get('Ip_remoto'),
        host_name=session.get('host_name'),
        current_time=datetime.utcnow()
    )

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
