from pprint import pprint
import requests

bot_token = "579475538:AAFjEgtt1BFPIU_f4IjYyaix-heREgouX3g"
test_url = "https://3b21cdb2.ngrok.io/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())