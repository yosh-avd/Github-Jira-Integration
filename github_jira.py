from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://yoshobanta-153.atlassian.net/jira/rest/api/3/issue"
    
    API_TOKEN= "ATATT3xFfGF0TIhvHj1aqwhQGDdQZZiX6c8_xhQkBLRUr7iv5_S8YiBqaknan2auH7n6964ZROMeRLLzR9nMFeG7t5scATq_CSHTk_YrHfcvPtfp7zp4JaMqQVTJaf4WrN4iNH3NMR8JP8bt72W0W9RMNG7AiUI7l_TX_VLzwMjXFc-2_Xa_krg=C6481326"
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