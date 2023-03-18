from flask import Flask, g
from blog.user import views
from blog.models.database import db
from flask_migrate import Migrate
from blog.views.authors import authors_app
from blog.admin import admin


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(views.user)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(authors_app, url_prefix="/authors")


cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")
migrate = Migrate(app, db)

@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")

admin.init_app(app)