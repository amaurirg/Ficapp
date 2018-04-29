from uber_rides.auth import AuthorizationCodeGrant
from uber_rides.session import Session
from uber_rides.client import UberRidesClient


auth_flow = AuthorizationCodeGrant(
    '-iiIrHNDDp5khRs_dpGqq0rBvRwd1dQn',
    ['places', 'profile', 'all_trips'],
    'wScfIhscTdyv8dWw26Bb7M2899limPKQ1rF6CrZI',
    # 'KA.eyJ2ZXJzaW9uIjoyLCJpZCI6IjQ3WTlLcUl1VFNtbTdkWmJadVNVb2c9PSIsImV4cGlyZXNfYXQiOjE1MjcxMzI5MzgsInBpcGVsaW5lX2tleV9pZCI6Ik1RPT0iLCJwaXBlbGluZV9pZCI6MX0.DktH6vbpWIbh8qNMnduygBrvS3l-nvJD3wctIjftMx8',
    'http://localhost:8000'
)
auth_url = auth_flow.get_authorization_url()

print(auth_url)

# session = auth_flow.get_session(redirect_uri)
# client = UberRidesClient(session, sandbox_mode=True)
# credentials = session.oauth2credential

# print(auth_flow.state_token)
# print(auth_flow.client_id)
# print(auth_flow.get_authorization_url())
# print(auth_flow.redirect_url)
# print(auth_flow.scopes)
# session = Session(server_token='Ls6hCxMf0l3ZFM0qaD5RVHbfgASx8oGPLRHsXVb4')
# print(session)
# session = auth_flow.get_session(redirect_url='http://localhost:8000/autorization')
# print(session)

# client = UberRidesClient(session, sandbox_mode=True)

# print(UberRidesClient(session, sandbox_mode=True))
# print(session.oauth2credential)