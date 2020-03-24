from flask import Flask
from flask import abort
from flask import request
import json
app = Flask(__name__)
import http.server
import socketserver

@app.route('/register', methods =['PUT'])
def register():
    req_data = request.json()
    print(req_data)
    hostname = req_data['hostname']
    ip = req_data['ip']
    as_ip = req_data['as_ip']
    as_port = req_data['as_port']
    url = "http://" + as_ip+":"+as_port+"/registerdns"
    data = {
            "TYPE" : "A",
            "NAME" : hostname,
            "VALUE": ip,
            "TTL" : 10,
        }
    data_json = json.dumps(data)
    r = request.post(url,data_json)
    return r 

@app.route('/fibonacci')
def RespondFib():
    num=request.args.get('number')
    return Calculatefibonacci(num)

def Calculatefibonacci(num):
    
    f=0
    if num == 0: 
        return 0
    memo = []
    for n in memo:
        f= memo[n]
    if num<=2 : 
        f=1
    else:
        f = Calculatefibonacci(num-1) +Calculatefibonacci(num-2)
    return f 
app.run(host='0.0.0.0',
        port=9090,
        debug=True)