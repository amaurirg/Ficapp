from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from uber_rides.auth import AuthorizationCodeGrant
from uber_rides.session import Session
from uber_rides.client import UberRidesClient


def home(request):
    return render(request, "index.html")


@csrf_exempt
def event(requests):
    print(requests.body)
    # return JsonResponse({'status': 'true', 'message': 'worked'})
    return HttpResponse()


def autorization(requests):
    auth_flow = AuthorizationCodeGrant(
    '-iiIrHNDDp5khRs_dpGqq0rBvRwd1dQn',
    ['places', 'profile', 'all_trips'],
    'wScfIhscTdyv8dWw26Bb7M2899limPKQ1rF6CrZI',
    'http://localhost:8000'
    )
    auth_url = auth_flow.get_authorization_url()
    return render(auth_url, 'autorization.html')


'''
redirect_url = 'http://localhost:8000/'
session = auth_flow.get_session(redirect_url)
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oauth2credential
'''