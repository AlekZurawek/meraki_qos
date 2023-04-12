import requests
import json

api_key = "x"
base_url = "https://api.meraki.com/api/v1"

headers = {
    "X-Cisco-Meraki-API-Key": api_key,
    "Content-Type": "application/json"
}

example_network_id = "y"
get_rules_url = f"{base_url}/networks/{example_network_id}/appliance/trafficShaping/rules"

response = requests.get(get_rules_url, headers=headers)
if response.status_code == 200:
    rules = response.json()

    with open("networks.conf", "r") as f:
        network_ids = [line.strip().split()[0] for line in f.readlines()]

    for network_id in network_ids:
        put_rules_url = f"{base_url}/networks/{network_id}/appliance/trafficShaping/rules"
        put_response = requests.put(put_rules_url, headers=headers, data=json.dumps(rules))

        if put_response.status_code == 200:
            print(f"Successfully copied rules to network {network_id}")
        else:
            print(f"Failed to copy rules to network {network_id}: {put_response.text}")

else:
    print("Failed to get rules from example network")
