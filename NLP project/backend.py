from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Recipe database (per person quantity)
recipes = [
    {
        "name": "Tomato Rice 🍅🍚",
        "ingredients": {
            "rice": 100,
            "tomato": 1,
            "onion": 0.5,
            "spices": 5
        }
    },
    {
        "name": "Egg Curry 🥚",
        "ingredients": {
            "egg": 2,
            "onion": 0.5,
            "tomato": 1,
            "spices": 5
        }
    },
    {
        "name": "Chicken Biryani 🍛",
        "ingredients": {
            "rice": 120,
            "chicken": 150,
            "onion": 1,
            "spices": 10
        }
    },
    {
        "name": "Veg Sandwich 🥪",
        "ingredients": {
            "bread": 2,
            "tomato": 0.5,
            "cucumber": 0.5,
            "butter": 10
        }
    }
]

@app.route("/find-recipe", methods=["POST"])
def find_recipe():
    data = request.json
    ingredients = data.get("ingredients", [])
    members = data.get("members", 1)

    if members < 1 or members > 1000:
        return jsonify({"error": "Members must be between 1 and 1000"})

    results = []

    for recipe in recipes:
        keys = recipe["ingredients"].keys()

        # check match
        if any(item in keys for item in ingredients):

            scaled = {}
            for item, qty in recipe["ingredients"].items():
                scaled[item] = qty * members

            results.append({
                "name": recipe["name"],
                "ingredients": scaled
            })

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)