from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

from api.models import User

import os

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'blog',
    'host': os.getenv("MONGO_URI")
}
db = MongoEngine(app)


@app.route("/", methods=["GET", "POST"])
def users():

    if request.method == "POST":
        data = request.get_json()

        user = User(name=data.get("name"), age=int(data.get("age")))
        user.save()

    users = User.objects()
    return jsonify({"users": users})
