import requests, json

username = '1234567890'
password = 'xxxxxxxx'

base_url = "https://api.janja.me"
url = "{}/v0/messages/text".format(base_url)
#url = "{}/v0/messages/sendimage".format(base_url)

payload = json.dumps({
  "to_phonenumber": "256782119329",
  "sender_id": "256779096531",
  "message": "Test Message 2"
})

'''
payload = json.dumps({
  "to_phonenumber": "256782119329",
  # "sender_id": "256779096531",
  "sender_id": "256783997272",
  "image_url": "https://media-exp1.licdn.com/dms/image/C4D03AQHJeferdeazfQ/profile-displayphoto-shrink_100_100/0/1517370997305?e=1650499200&v=beta&t=-GTdOxN5zAPTr8uj5Dn_Q3jFqoF0TrD95vrHgCvKsiM",
  "caption": "Dummy Image"
})
'''


def send_im(to_phonenumber, message):
  payload = {
    "sender_id": "256783997272",
    "to_phonenumber": to_phonenumber,
    "message": message
  }
  response = requests.request("POST", url, json=payload,
                              auth=(username, password))

  return response
# print(response.text)