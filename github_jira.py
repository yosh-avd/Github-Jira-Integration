from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://yoshobanta-153.atlassian.net/rest/api/3/issue"
    
    API_TOKEN= "ATATT3xFfGF0Hj-pHsmB39jxammRd4VoFkC8w63VzjQDkhSF_QRBKcjQ95Zi2BDchmxBYd4BoJfxBZ6jdK2Mo0geBWYD9M8Y697KNMIqKtGZ0NvBGTENWEvdgtoM8GeSHKpEd9AOlWrGosr6UlEeRDxz79BB57En_P-PQl_mV01JNnsd4Ybt5-g=E7CBAE80"
    auth = HTTPBasicAuth("garnaikyosh@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "MAH"
        },
        "issuetype": {
            "id": "10007"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)