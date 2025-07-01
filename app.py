from flask import Flask
from routes import bp

app = Flask(__name__)
app.secret_key = "BEATIFULPENISYEAH"
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)