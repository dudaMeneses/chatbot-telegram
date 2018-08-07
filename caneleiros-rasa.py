import logging
import requests
import json
from flask import Flask, request

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)
logger = logging.getLogger(__name__)

bot_token = "579475538:AAFjEgtt1BFPIU_f4IjYyaix-heREgouX3g"

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def process_message(update):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]

    url = "http://localhost:5050/parse"
    query = json.dumps({"q":update["message"]["text"].encode("utf-8")})

    rasaResponse = requests.post(url, data=str(query))

    logging.info(rasaResponse.json())

    if rasaResponse.status_code == requests.codes.ok:
        data["text"] = rasaResponse.json()["intent"]["name"]
    else:
        data["text"] = "Nao te entendi, brother"

    r = requests.post(get_url("sendMessage"), data=data)

@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            process_message(update)
        return "ok!", 200