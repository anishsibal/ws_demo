from flask import Flask
from flask import jsonify
from flask import request
import re

import datetime
app = Flask(__name__)
app.config.from_object('config')
LOG_LOCATION = app.config['LOG_FILE']
now = datetime.datetime.now()
data = {}
data['siteUpSince'] = now
data['IPs'] = {}

with open(LOG_LOCATION) as fh:
 for line in fh:
     ip = line.split()[0]
     if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip):
         print(ip)
         if ip in data['IPs']:
             data['IPs'][ip] += 1
         else:
             data['IPs'][ip] = 1
     else:
         continue

@app.route('/')
def uptimeAndIps():
    ip = request.remote_addr
    if ip in data['IPs']:
	    data['IPs'][ip] += 1
    else:
	    data['IPs'][ip] = 1
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
