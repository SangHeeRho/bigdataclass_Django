from flask import Flask, jsonify, render_template, request

import ml_sanghee

app = Flask(__name__)

# 템플릿 자동 리로딩
app.config['TEMPLATES_AUTO_RELOAD'] = True


# 브라우저로 http://localhost:5000 주소 접속하시면, hello world 메세지


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    expected = {}
    for name, f in request.files.items():
        expected_number = ml_sanghee.predict(f)
        expected[name] = expected_number

    return jsonify(expected)
