import requests
from datetime import datetime
USERNAME = "aelsheikh20202023"
TOKEN = "soft_2020"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_prams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_prams)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# print(today.strftime("%Y%m%w"))
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2023, month=7, day=15)
yesterday_formatted = yesterday.strftime("%Y%m%d")
today = datetime.now()

graph_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=graph_data, headers=headers)
print(response.text)


pixela_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"

graph_update = {
    "quantity": "20"
}

# response = requests.put(url=pixela_update_endpoint, json=graph_update, headers=headers)
# print(response.text)


pixela_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
# response = requests.delete(pixela_delete_endpoint, headers=headers)
# print(response.text)