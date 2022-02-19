import random

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

import requests
from janja.api import send_im
from api.models import JanjaSession

BASE_URL = 'http://54.186.202.6:8888/ussd/255'
# ?INPUT=255&SessionId=1645068896&MSISDN=256756666333&IMSI=641010247712386&TYPE=1'
# Create your views here.
class ApiEndpointView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)


        phone_number = request.POST.get('sender_id')
        user_input = request.POST.get('user_response')
        full_name = request.POST.get('full_name')

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
        print(f'UUSD Resp: {resp.text}')

        response = send_im(phone_number, resp.text)
        print(f'Whatsapp resp: {response.text}')
        return HttpResponse('Ok')