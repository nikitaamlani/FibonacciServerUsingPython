import json   
from flask import abort                                                   

from flask import Flask, request                                

app = Flask(__name__)                                           

                                    

@app.route('/registerdns',methods=['GET','POST'])            
def dns():                                           
    posted_data = json.load(request.files['data_json'])             
    with open('fibDetailsS.txt', 'w') as json_file:
        json.dump(posted_data, json_file)
    return '201' 

@app.route('/dnsquery',methods=['GET','POST'])            
def dnsquery():   
    posted_data = json.load(request.files['data_json'])  
    if posted_data['TYPE'] == 'A' and posted_data['NAME'] == 'fibonacci.com':                                      
        with open('fibDetailsS.txt','r') as json_file:
            data = json.load(json_file)
            response = {
                "TYPE" : data["TYPE"],
                "NAME" : data["NAME"],
                "VALUE": data["VALUE"],
                "TTL" : data["TTL"],
            }
        return response
    else:
        return abort(400)
app.run(host='0.0.0.0',
        port=53533,
        debug=True)