# ws_demo
WebServer Tracking Demo

## Getting Started

### Clone the repository
```
git clone git@github.com:anishsibal/ws_demo.git
```
### Rename and update file "variables.tf.required"
```
mv variables.tf.required variables.tf
```
Edit variables.tf and your credentails, keys and OCIDs. They are required to make connection to Oracle Cloud. Replace
the following with your info:
```
<ADD_TENANCY_OCID>

<ADD_COMARTMENT_OCID>

<API_FINGERPRINT>

<PRIVATE_KEY_PATH>

<SSH_PUBLIC_KEY>

<USER_OCID>

<SUBNET_OCID>

<OS_IMAGE_OCID>
```
### Now run terraform init and apply
```
terraform init .
terraform apply .
```

Once the above is run, the cloud init bootstrap will start the flask server app.
The output of terraform apply, will show the Public address as well. 

You can go to public ip address , and it will show the json output with Site uptime and client IP visit tracking.

You can also run curl command on ip address, e.g.:
```
$ curl 129.213.130.114
{"IPs":{"104.192.200.117":1,"24.27.53.151":5},"siteUpSince":"Tue, 21 Aug 2018 20:07:09 GMT"}
$ curl 129.213.130.114
{"IPs":{"104.192.200.117":1,"24.27.53.151":6},"siteUpSince":"Tue, 21 Aug 2018 20:07:09 GMT"}
$
```

### Manual Setup wihtout using Oracle Cloud Infra

Install python 2.x, pip and git on your machine. Perform below tasks as root or sudo

Install flask 
```
pip install flask
```
Clone repo 
```
mkdir -p /ws_demo
cd /ws_demo
git clone https://github.com/anishsibal/ws_demo .
```
Create log dir 
```
mkdir -p /var/log/ws_demo
```

Start flask app
```
cd /ws_demo/app
python app.py >> /var/log/ws_demo/app.log 2>&1 &
```

NOTE: If machines on network need to access the app server, port 80 needs to be opened on the local machine

Testing on local machine
```
curl http://127.0.0.1
````
```
