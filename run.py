from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "hardsecretkey"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345678@db:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<{self.name}>"


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return f"<{self.username}>"


@app.route("/")
def index():
    return "<h1> Hello world 3 </h1>"


if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True)
