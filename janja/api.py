import requests, json

username = '1234567890'
password = 'xxxxxxxx'

base_url = "https://api.janja.me"
url = "{}/v0/messages/text".format(base_url)

def send_im(to_phonenumber, message):
  payload = {
    "sender_id": "256782XXXXXX",
    "to_phonenumber": to_phonenumber,
    "message": message
  }
  response = requests.request("POST", url, json=payload,
                              auth=(username, password))

  return response
# print(response.text)