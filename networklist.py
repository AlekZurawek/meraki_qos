import requests

api_key = "x"
base_url = "https://api.meraki.com/api/v1"
organization_id = "x"

headers = {
    "X-Cisco-Meraki-API-Key": api_key,
    "Content-Type": "application/json"
}

get_networks_url = f"{base_url}/organizations/{organization_id}/networks"

response = requests.get(get_networks_url, headers=headers)

if response.status_code == 200:
    networks = response.json()

    with open("list_of_networks.txt", "w") as f:
        for network in networks:
            f.write(f"{network['id']} {network['name']}\n")
    print("Successfully saved network IDs and names to list_of_networks.txt")
else:
    print("Failed to get networks from the organization")
