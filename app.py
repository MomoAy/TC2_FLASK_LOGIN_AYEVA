from app import create_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = create_app()

#creer la table dans la BD
with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)
