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

Once the above is run, the cloud init bootstrap will start the flask server with app /app.py.
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
