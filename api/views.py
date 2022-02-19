import random, json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import requests
from janja.api import send_im
from api.models import JanjaSession

BASE_URL = 'http://54.186.202.6:8888/ussd/255'
# ?INPUT=255&SessionId=1645068896&MSISDN=256756666333&IMSI=641010247712386&TYPE=1'

class ApiEndpointView(View):
    def post(self, request, *args, **kwargs):
        my_bytes_value = request.body
        my_json = my_bytes_value.decode('utf8').replace("'", '"')
        print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = data
        #s = json.dumps(data, indent=4, sort_keys=True)
        print(s)

        phone_number = s.get('sender_id')
        user_input = s.get('user_response')
        full_name = s.get('full_name')

        if user_input.lower() in ['menu', 'cancel', 'back', '255']:
            ussd_input = '255'
            ussd_session_id = random.randint(100000, 9999999)
            session = JanjaSession.objects.create(phone_number=phone_number, session_id=ussd_session_id)
        else:
            ussd_input = user_input
            session = JanjaSession.objects.filter(phone_number=phone_number).last()

        params = {
            'INPUT': ussd_input,
            'MSISDN': phone_number,
            'TYPE': 1,
            'SessionId': session.session_id,
        }

        print(f'Sending USSD Req: {params}')
        resp = requests.get(BASE_URL, params=params)
        print(f'USSD Resp: {resp.text}')

        response = send_im(phone_number, resp.text)
        print(f'Whatsapp resp: {response.text}')
        return HttpResponse('Ok')