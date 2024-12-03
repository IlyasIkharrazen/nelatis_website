from flask import Flask
 
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
 
    from .routes import main
    app.register_blueprint(main)
 
    return app

# Démarrer l'application si le fichier est exécuté directement
if __name__ == "__main__":
    app = create_app()
    # Utilisez la variable d'environnement PORT définie par Render
    import os
    port = int(os.environ.get("PORT", 5000))  # Par défaut, utilisez le port 5000
    app.run(host="0.0.0.0", port=port)

