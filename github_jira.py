from flask import Flask,request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://yoshobanta-153.atlassian.net/rest/api/3/issue"
    
    API_TOKEN= "ATATT3xFfGF0V2p7xW4x-WxQ4aysVN3SawQLze35y9Ik4drmviQFTa5flxdNaHnO7mQaDgw6iZEQnEm2vtP8XPlhgcbJw86Y7-JkYwjGGw-Om6azz43nrRIvLarzKHFP97ylV8hstBS_rZsfytajycb5R8HAy74T6A0MTZf5ZWQT5okuSof9lG4=05B5578A"
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
        "summary": "jira_Main order flow broken",
    },
    "update": {}
    } )

    webhook = request.get_json()

    required_output = webhook['comment'].get('body')

    if (required_output  == '/jira'):
            response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
            )

            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    else:
            print("Jira issue will be created if comment include /jira")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)