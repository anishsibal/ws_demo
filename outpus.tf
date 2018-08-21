#This file controls the list of values displayed at the end of the terraform apply.
output "ws_demo-1" {
  value = "${oci_core_instance.ws_demo-1.public_ip}"
}
