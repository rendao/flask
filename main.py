from flask import Flask, jsonify,request
import os
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/message',methods = ['POST'])
def mess():
    sk = request.json.get('openaikey')
    msg = request.json.get('msg')
    url = request.json.get('url')
    print(sk,msg,url)
    req = requests.post(url,json=msg , headers={'content-type': 'application/json', 'Authorization': 'Bearer ' + sk})
    print(req.status_code)
   
    if req.status_code == 200:

        reqdic = json.loads(req.text)
        print(reqdic)
        # aa = reqdic['choices'][0]['text']
        res = {
            "resmsg":reqdic,
            "code":200
        }
        return res
    else:
        reqdic = json.loads(req.text)
        err = reqdic['error']['message']
        res = {
            "resmsg":err,
            "code":412
        }
        return res

@app.route('/quota',methods = ['POST'])
def quota():
    sk = request.json.get('openaikey')
    print(sk)
    req = requests.get('https://api.openai.com/dashboard/billing/credit_grants' , headers={'content-type': 'application/json', 'Authorization': 'Bearer ' + sk})
    print(req.status_code)
   
    if req.status_code == 200:

        reqdic = json.loads(req.text)
        print(reqdic)
        # aa = reqdic['choices'][0]['text']
        res = {
            "resmsg":reqdic,
            "code":200
        }
        return res
    else:
        reqdic = json.loads(req.text)
        err = reqdic['error']['message']
        res = {
            "resmsg":err,
            "code":412
        }
        return res

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
