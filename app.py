from flask import Flask
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    LOG.info(f"Udacity Final Prject Capstone ")
    html = f"<h3>Udacity Final Prject Capstone </h3>"
    return html.format(format)

if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
