# imports
# let's try functions throughout

from flask import Flask, request
import json

# Creating an instance of the Flask class
app = Flask(__name__)

# Routing
@app.route("/", methods = ["POST"])
def ussd():

    # Reading variables sent via POST from Africa's Talking's API
    session_id = request.values.get("SessionId", None)
    service_code = request.values.get("ServiceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    # Price
    price = "0.20"

    # Reading data from nominees.json
    with open("nominees.json", "r") as f:
        data = json.load(f)
        codes = data.keys()

    if text == "":
        # Initial response
        response = "CON Welcome to VoteYou \n\n"
        response += "Please Enter Nominee's code"
    

    elif text.upper()[:2] in codes:
        requested_code = text.upper()[:2]
        nominee_number = text[3:]
        
        if nominee_number in data[requested_code]["Nominees"].keys() :

            nominee = data[requested_code]["Nominees"][nominee_number]
            response = f"CON Nominee Name: {nominee}"
            response += f"Price of Vote: GHS {price}"
        
        else:
            response = "CON Sorry, Please try again. END"
    
    elif int(text):
        total_amount = int(text) * price
        response = f"CON You are voting {int(text)} times for {data[]}"

    else:
        response = "CON Sorry, Please try again. END"