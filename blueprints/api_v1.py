from flask import Flask, jsonify, Blueprint
from flask_restplus import Api, Resource
from common import *

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')

api = Api(api_v1,
        version='1.0',
        title='CertAPI',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        contact="@jasper9")



# ENDPOINTS ############################################################################################################
# ######################################################################################################################

# Example Usage
# curl http://localhost/api/v1/cert/josh_domain.com
@api.route('/cert/<domain>')
@api.doc(params={
                    'domain': 'Domain to generate certificate for'
            })
class cert(Resource):
    def get(self, domain):
        '''Generate Certificate'''
        
        # If response in json format
        #txt = ["cert"]
        # magic here
        #return jsonify(txt)

        resp = generateCert(domain)

        return(resp)

# ######################################################################################################################
