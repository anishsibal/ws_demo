resource "oci_core_instance" "ws_demo-1" {
  #Required
  availability_domain = "${var.availability_domain}"
  compartment_id = "${var.compartment_ocid}"
  shape = "${var.instance_shape}"

  create_vnic_details {
  	#Required
  	subnet_id = "${var.subnet_ocid}"
  	#Optional
  	assign_public_ip = true
  }
  metadata {
		ssh_authorized_keys = "${var.ssh_authorized_keys}"
    user_data = "${base64encode(file(var.BootStrapFile))}"
	}
  source_details {
	    #Required
	    source_type = "image"
	    source_id = "${var.image_ocid}"

	}
}

