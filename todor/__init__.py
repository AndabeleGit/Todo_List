from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG=False,
        SECRET_KEY='devTodo',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )

    db.init_app(app)

    # Mover las importaciones aquí para evitar el ciclo de importación
    from . import todo, auth

    # Registro Blueprint
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app
