from flask import Flask
from flask import jsonify
from flask import request

import datetime
app = Flask(__name__)
now = datetime.datetime.now()
print(now)
data = {}
data['siteUpSince'] = now
data['IPs'] = {}
print(now)
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
