import requests
import json
from flask import Flask, render_template, request

response = {"status": "O"}
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        card = request.form.get("card")
        amount = request.form.get("amount")
        date = request.form.get("date")
        command = request.form.get("command")
        refnum = request.form.get("card")
        transactions = {
          "card": card, "amount": amount, "date": date, "command": command, "refnum": refnum
        }
      
    
    
        url = "https://x1.cardknox.com/gatewayjson"

        if transactions["command"] == "Sale":
          type = "1"
        elif transactions["command"] == "Authorization":
          type = "2"
        elif transactions["command"] == "Capture":
          type = "3"
        elif transactions["command"] == "Void":
          type = "4"
        else:
            print("Okay")
        if type == "1":
            xcommand = "cc:sale"
            xcardnum = transactions["card"]
            xexp = transactions["date"]
            xammount = transactions["amount"]
            payload = json.dumps({
              "xcardnum": xcardnum,
              "xexp": xexp,
              "xkey": "artemisdev9d423588838a438f9036c65c3318140c",
              "xversion": "4.5.9",
              "xsoftwarename": "Nosson",
              "xsoftwareversion": "2.3.5",
              "xcommand": xcommand,
              "xamount": xammount,
              "xallowduplicate": "True"
            })
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            print(response)
            if response["xResult"] == "A":
                return render_template("form2.html")
            elif response["xResult"] == "E" or response["xResult"] == "D":
                return render_template("form3.html")
        elif type == "2":
            xcommand = "cc:authonly"
            xcardnum = transactions["card"]
            xexp = transactions["date"]
            xammount = transactions["amount"]
            payload = json.dumps({
              "xcardnum": xcardnum,
              "xexp": xexp,
              "xkey": "artemisdev9d423588838a438f9036c65c3318140c",
              "xversion": "4.5.9",
              "xsoftwarename": "Nosson",
              "xsoftwareversion": "2.3.5",
              "xcommand": xcommand,
              "xamount": xammount,
              "xallowduplicate": "true"
            })
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            print(response)

        elif type == "3":
            xcommand = "cc:capture"
            xrefnum = transactions["refnum"]
            payload = json.dumps({
              "xkey": "artemisdev9d423588838a438f9036c65c3318140c",
              "xversion": "4.5.9",
              "xsoftwarename": "Nosson",
              "xsoftwareversion": "2.3.5",
              "xcommand": xcommand,
              "xrefnum": xrefnum
            })
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            print(response)

        elif type == "4":
            xcommand = "cc:void"
            xrefnum = transactions["refnum"]
            payload = json.dumps({
              "xkey": "artemisdev9d423588838a438f9036c65c3318140c",
              "xversion": "4.5.9",
              "xsoftwarename": "Nosson",
              "xsoftwareversion": "2.3.5",
              "xcommand": xcommand,
              "xrefnum": xrefnum
            })
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            print(response)
            
        else:
            print("Sorry, that was not one of the option provided")
            exit()
            
    return render_template("form.html")  

if __name__ == "__main__":
  app.run(debug=False, host="0.0.0.0", port=80)