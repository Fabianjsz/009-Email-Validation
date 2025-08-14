import os, requests

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")


def check_Email():
    email = input("Welche E-Mail soll überprüft werden?")
    url = f"http://apilayer.net/api/check?access_key={API_KEY}&email={email}"
    response = requests.get(url+"callback=CALLBACK_FUNCTION")

    if response.status_code == 200:
        print(f"Passed")
        response = response.json()
        return response
    else:
        print(f"Failed; status:{response.status_code}")


print(check_Email())
