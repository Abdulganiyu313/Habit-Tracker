import requests
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv(dotenv_path=Path(".env"))

# Get credentials from .env
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")

# Base endpoints
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def create_graph():
    """Create the Pixela graph (run only once)."""
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "hours",
        "type": "float",
        "color": "shibafu"
    }
    res = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    print("Graph:", res.status_code, res.text)


def log_habit(quantity):
    """Log today's habit data (POST request)."""
    today = datetime.datetime.now().strftime("%Y%m%d")
    pixel_data = {
        "date": today,
        "quantity": str(quantity)
    }
    res = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=HEADERS)
    print("Log Habit:", res.status_code, res.text)


def delete_pixel(date):
    """Delete a pixel for a specific date."""
    endpoint = f"{POST_PIXEL_ENDPOINT}/{date}"
    res = requests.delete(url=endpoint, headers=HEADERS)
    print("Delete Pixel:", res.status_code, res.text)


def update_pixel(date, new_quantity):
    """Update a pixel entry."""
    endpoint = f"{POST_PIXEL_ENDPOINT}/{date}"
    data = {"quantity": str(new_quantity)}
    res = requests.put(url=endpoint, json=data, headers=HEADERS)
    print("Update Pixel:", res.status_code, res.text)


if __name__ == "__main__":
    print("📊 Welcome to your Habit Tracker!")

    choice = input("Do you want to [L]og, [U]pdate, [D]elete, or [C]reate graph? ").strip().upper()

    if choice == "C":
        create_graph()
    elif choice == "L":
        hours = input("Enter number of hours you coded today: ")
        log_habit(hours)
    elif choice == "U":
        date = input("Enter date to update (YYYYMMDD): ")
        qty = input("Enter new quantity: ")
        update_pixel(date, qty)
    elif choice == "D":
        date = input("Enter date to delete (YYYYMMDD): ")
        delete_pixel(date)
    else:
        print("Invalid option. Please try again.")
