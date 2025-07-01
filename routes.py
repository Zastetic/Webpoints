from database import *
from flask import render_template, request, redirect, Blueprint, jsonify, url_for
from flask import session as user_session

bp = Blueprint("main", __name__)

USER = "admin"
PASSWORD = "1234"


# API's -------------------------
@bp.route("/set-periodo", methods=["POST"])
def set_periodo():
    data = request.get_json()
    user_session['periodo'] = data.get('periodo')

    return jsonify(status='ok', periodo=user_session['periodo'])


@bp.route("/classes-name")
def get_names():
    if "periodo" not in user_session:
        user_session['periodo'] = 'Classe_manha'

    return jsonify({"names": [c.nome for c in session.query(globals()[user_session["periodo"]]).all()]})

@bp.route("/classes-points")
def get_points():
    if 'periodo' not in user_session:
        user_session['periodo'] = 'Classe_manha'

    return jsonify({"names": [c.ponto for c in session.query(globals()[user_session["periodo"]]).all()]})

# PAGINAS INICIAIS ------------------------------
@bp.route("/")
def index():
    return render_template('main_page.html')
@bp.route('/rules')
def rules():
    return "Tem regra aqui em"

@bp.route('/ranking')
def ranking():
    return render_template("ranking.html")

@bp.route('/pontuation')
def pontuation():
    return "aq tem uns pontos em"

# PAGINAS DE ADM ------------------------------------

# ROTA DE LOGIN
@bp.route('/adm-login-page', methods=["POST", "GET"])
def adm_login_page():
    if request.method == "POST":
        senha  = request.form["password"]
        usuario = request.form["username"]
        print(senha, usuario)

        if senha == PASSWORD and usuario == USER:
            user_session['autenticado'] = True
            print(user_session['autenticado'])
            return redirect(url_for("main.admin"))
        else:
            print("senha errada aiai")
        
    return render_template('adm-login-page.html')
    
# PAGINA DE ADM
@bp.route('/admin', methods=['POST', 'GET'])
def admin():
    # Recusa coneção se user_session não estiver autenticado
    if not user_session.get('autenticado'):
        return redirect("/adm-login-page")
    
    CASA = globals()[user_session["periodo"]]
    print(CASA)
    # Verifica requisição POST de formulario
    if request.method == "POST":

        print(request.form.get("casa"))
        
        if request.form.get("casa"):
            nome_casa = request.form["casa"]

            print(nome_casa)
            SQL_points = session.query(CASA.ponto).filter(CASA.nome == nome_casa).scalar() # Pega a quantidade de pontos atual de determinada casa
            if request.form.get("acao") == "adicionar" or request.form.get("acao") == "remover":
                add_points = SQL_points - int(request.form["pontos"]) if request.form.get("acao") == "remover" else SQL_points + int(request.form["pontos"])
                casa_requery = session.query(CASA).filter_by(nome=nome_casa).update({"ponto" : add_points })

                session.commit() # Adiciona pontos modificados ao banco de dados
    
        return redirect(url_for('main.admin'))
    return render_template('admin-control-panel.html')


@bp.route("/modify_points", methods=["GET"])
def mod_points():
    nome_casa = request.args.get("casa")
    pontos = request.args.get("pontos")

    CASA = globals()[user_session["periodo"]]

    print(nome_casa, pontos)

    SQL_points = session.query(CASA.ponto).filter(CASA.nome == nome_casa).scalar()

    add_points = SQL_points + int(pontos)
    casa_requery = session.query(CASA).filter_by(nome=nome_casa).update({"ponto" : add_points })
    session.commit()

    return redirect(url_for("main.admin"))



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("adm-login-page"))