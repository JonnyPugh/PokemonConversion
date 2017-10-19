from flask import *
from requests import get

main = Blueprint("main", __name__, template_folder="templates")
@main.route("/")
def index():
	return render_template("index.html")

pokemon_blueprint = Blueprint("pokemon", __name__)
@pokemon_blueprint.route("/api/v1/pokemon", methods=["GET"])
def pokemon():
	try:
		weight = float(request.args["weight"])
		if weight <= 0:
			return jsonify({"error": "Weight cannot be 0 or negative"}), 400
		r = get("http://pokeapi.co/api/v2/pokemon/" + request.args["pokemon"])
		r.raise_for_status()
		return jsonify({"conversion": weight / (r.json()["weight"] / 10.0)})
	except Exception as e:
		return jsonify({"error": "Specified Pokemon does not exist"}), 404

app = Flask(__name__, template_folder="templates")
app.register_blueprint(main)
app.register_blueprint(pokemon_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
