#!/usr/bin/env python3

import typer
import os
import requests

app = typer.Typer()

@app.command()
def ping():
    try:
        url = "http://" + str(os.environ['API_HOST_TEST']) + "/"
        print(url)
        response = requests.get(url)
        print(response.content)
    except KeyError:
        print("variable not set")

@app.command()
def merge(seq): 
    try:
        url = "http://" + str(os.environ['API_HOST_TEST']) + "/api/v1/action/mergeV2"
        print(url)
        try:
            response = requests.post(url,json={"name":seq})
            print(response.content)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("An error occurred performing request")
            print(e)
    except KeyError:
        print("variable not set")

@app.command()
def invoke(action,params): 
    try:
        url = "http://" + str(os.environ['API_HOST_TEST']) + "/api/v1/action/invoke-with-params"
        print(url)
        try:
            response = requests.post(url,json={"name":action ,"params":params})
            print(response.content)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("An error occurred performing request")
            raise SystemExit(e)
    except KeyError:
        print("variable not set")

if __name__ == "__main__":
    app()



