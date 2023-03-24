from flask import Flask
import datablitz

app = Flask(__name__)


@app.route('/nsw')
def index():
    return datablitz.data_nsw


if __name__ == '__main__':
    app.run(debug=True)
