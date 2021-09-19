#!/usr/bin/python3

"""
    Python script that show the user information.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
        get request to https://random-data-api.com/api/internet_stuff/
        random_internet_stuff with
        the name as a parameter.
    """
    try:
        url = "https://random-data-api.com/api/internet_stuff" \
              "/random_internet_stuff"
        request = requests.get(url).json()
        type = request['user_agent']
        print("L'adresse email de l'utilisateur {}  est {} . "
              "Iel utilise le système d'exploitation {}"
              .format(request['email'],
                      request['username'],
                      request['user_agent'][13:21]))
    except ValueError:
        print("Not a valid URL")
