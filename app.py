from flask import Flask, render_template
from satellites import get_sat_info

app = Flask(__name__)

sat_info = get_sat_info()

@app.route("/")
def hello_world():
    return render_template('index.html', sat_info=sat_info)