from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .routes import main
    app.register_blueprint(main)

    return app

# Ajouter cette ligne pour exposer l'instance Flask
app = create_app()


