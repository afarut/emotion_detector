#EXAMPLE OF USING


from flask import Flask, jsonify, request, render_template
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)


# Cross Origin Resource Sharing (CORS) handling


@app.route('/upload', methods=["POST"])
def upload_form():
    data = request.form.to_dict()
    return jsonify(data)


@app.route('/', methods=["POST", "GET"])
def index():
    data = {}
    if request.method == "POST":
        tmp = request.form.to_dict()
        data["partydate"] = tmp["partydate"]
        data["title"] = tmp["title"]
        title = f"{data['title']}datetime_{data['partydate']}".replace(":", "_")
        file = request.files['file']
        print(title)
        path = "./static/before/" + title + "." + file.filename.split(".")[-1]
        #file.save(str(path))
        file.save(path)
    return render_template("index.html", post=request.method == "POST", **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555,debug=True)