from flask import Flask
from flask import abort
from flask import request
import json
app = Flask(__name__)
import requests

@app.route('/fibonacci',methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    url = "http://" +"localhost"+":"+as_port+"/dnsquery"
    datato = {
            "TYPE" : "A",
            "NAME" : hostname,
            }
    r = requests.post(url,data=datato)
    ipFib = r['VALUE']
    domainName = r['NAME']
    urlfib = "http://" +ipFib+"/"+domainName+"?"+"number="+number 
    ans = requests.post(urlfib)
    return ans

           
    

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
