from google.oauth2 import service_account

from google.auth.transport.requests import AuthorizedSession

import config
from webapp.resourceDefinition import makeLoyaltyClassResource

def makeOauthCredential():
    # the variables are in config file
    credentials = service_account.Credentials.from_service_account_file(
            config.SERVICE_ACCOUNT_FILE, scopes=config.SCOPES)

    return credentials

def getLoyaltyClassList():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    credentials = makeOauthCredential()
    
    response = None

    # Define get() REST call of target vertical
    uri = 'https://www.googleapis.com/walletobjects/v1'
    path = '/loyaltyClass?issuerId=3293346916822849083'# Resource representation is for an loyalty, so endpoint for loyaltyClass

    authed_session = AuthorizedSession(credentials)
    
    response = authed_session.get(
        uri+path          # REST API endpoint
        ,headers=headers  # Header; optional
    )
    
    return response

def insertLoyaltyClass(payload):

    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8'
        }
    credentials = makeOauthCredential()
    response = None

    # Define insert() REST call of target vertical
    uri = 'https://www.googleapis.com/walletobjects/v1'
    path = '/loyaltyClass' # Resource representation is for an loyalty, so endpoint for loyaltyClass

  # There is no Google API for Passes Client Library for Python.
  # Authorize a http client with credential generated from Google API client library.
  ## see https://google-auth.readthedocs.io/en/latest/user-guide.html#making-authenticated-requests
    authed_session = AuthorizedSession(credentials)

  # make the POST request to make an insert(); this returns a response object
  # other methods require different http methods; for example, get() requires authed_Session.get(...)
  # check the reference API to make the right REST call
  ## https://developers.google.com/pay/passes/reference/v1/offerclass/insert
  ## https://google-auth.readthedocs.io/en/latest/user-guide.html#making-authenticated-requests
    response = authed_session.post(
        uri+path          # REST API endpoint
        ,headers=headers  # Header; optional
        ,json=payload    # non-form-encoded Payload for POST. Check rest API for format based on method.
    )
    print(response.text)
    return response

if name == '__main__':
    classUid = "class_id_003"
    classId = '%s.%s' % (config.ISSUER_ID,classUid)
    issuerName = "Zaim Doverie"
    provider = "Qronus"
    programLogoUri = "https://farm66.staticflickr.com/65535/48486234062_d30e5b61f0.jpg"
    programName = "Our Loyalty Program"
    rgbcolor = "#ff01ff"
    classResourcePayload = makeLoyaltyClassResource(classId, issuerName, provider, programLogoUri,programName, rgbcolor)
    insertLoyaltyClass(classResourcePayload)