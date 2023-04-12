# meraki_qos
Copies MX QoS settings from one network to lots of networks. Untested in production script please use with caution!

Please use with caution and test prior using in production, this script comes with no warranties and is given as is.

How to run:
1. Edit networklist.py 

api_key = "x"
organization_id = "x"

Get organization_id from the bottom of the meraki.com page of the said organization, alternativly this can be obtain by simple API call.

2. Run networklist.py by running python3 networklist.py command
3. Configure QoS as per your desired configuration on one test network, get this network id from a new file created list_of_networks.txt
4. Edit lines qos.py

api_key = "x"
example_network_id = "y"

Where 'y' is enter network id of your source network from the file list_of_networks.txt this network should have all QoS configured as per your requirement.

5. Edit networks.conf file to include network id and name from the list_of_networks.txt file, be aware any network included in this file will automatically have its QoS settings copied from the previously defined example_network_id.
6. Run the qos.py script by running python3 qos.py command
7. Verify configuration by logging into Meraki dashboard

