from flask import Flask


app = Flask(__name__)

from app.clientes import main
app.register_blueprint(main)


app.run(debug=True,port=3000)

