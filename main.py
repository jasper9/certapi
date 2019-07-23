from flask import Flask, Blueprint
import configparser
from common import *

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

from blueprints.api_v1 import api_v1
app.register_blueprint(api_v1)

@app.before_request
def before_request():
    # This is run prior to each and every request

    # Here is where I would check the validity of the certificate that was created at start up
    #   and generate a new one if needed.

    print("Local system certificate looks ok!")


# Startup
print("Checking local certificate...")
generateCert(config['system']['domain'])

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True, threaded=True)
