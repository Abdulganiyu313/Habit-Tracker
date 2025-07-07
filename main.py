import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
DATE = "20250704"  # YYYYMMDD format
pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.datetime(year=2025, month=7, day=4)

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "timezone": "Africa/Lagos",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
    "timezone": "Africa/Lagos",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

post_graph_endpoint = f"{graph_endpoint}/graph1"

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

update_endpoint = f"{post_graph_endpoint}/{DATE}"
update_params = {
    "quantity": "15.0",
}

delete_endpoint = f"{post_graph_endpoint}/{DATE}"

print(f"Your graph: {post_graph_endpoint}")