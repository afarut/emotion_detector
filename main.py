#EXAMPLE OF USING


from flask import Flask, jsonify, request, render_template
import numpy as np


app = Flask(__name__)



# Cross Origin Resource Sharing (CORS) handling

@app.route('/', methods=["GET"])
def image_post_request():
	print(request.json)
	return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)