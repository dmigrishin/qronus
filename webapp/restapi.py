from google.oauth2 import service_account

from google.auth.transport.requests import AuthorizedSession

import config
import jwt
import json
from webapp.resourceDefinition import makeLoyaltyClassResource, makeLoyaltyObjectResource

def makeOauthCredential():
    # the variables are in config file
    credentials = service_account.Credentials.from_service_account_file(
            config.SERVICE_ACCOUNT_FILE, scopes=config.SCOPES)

    return credentials

def getLoyaltyObjectList():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    credentials = makeOauthCredential()
    
    response = None

    # Define get() REST call of target vertical
    uri = 'https://www.googleapis.com/walletobjects/v1'
    path = '/loyaltyObject?classId=3293346916822849083.class_id_003'# Resource representation is for an loyalty, so endpoint for loyaltyClass

    authed_session = AuthorizedSession(credentials)
    
    response = authed_session.get(
        uri+path          # REST API endpoint
        ,headers=headers  # Header; optional
    )
    
    return response

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

def insertOfferObject(payload):

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    credentials = makeOauthCredential()
    response = None

    # Define insert() REST call of target vertical
    uri = 'https://www.googleapis.com/walletobjects/v1'
    path = '/loyaltyObject' # Resource representation is for an Loyalty, so endpoint for loyaltyClass

    # There is no Google API for Passes Client Library for Python.
    # Authorize a http client with credential generated from Google API client library.
    ## see https://google-auth.readthedocs.io/en/latest/user-guide.html#making-authenticated-requests
    authed_session = AuthorizedSession(credentials)

    # make the POST request to make an insert(); this returns a response object
    # other methods require different http methods; for example, get() requires authed_Session.get(...)
    # check the reference API to make the right REST call
    ## https://developers.google.com/pay/passes/reference/v1/offerobject/insert
    ## https://google-auth.readthedocs.io/en/latest/user-guide.html#making-authenticated-requests
    response = authed_session.post(
        uri+path          # REST API endpoint
        ,headers=headers  # Header; optional
        ,json=payload    # non-form-encoded Payload for POST. Check rest API for format based on method.
    )
    print(response.text)
    return response

def insertNewLoyaltyObject():
    classUid = "class_id_003"
    classId = '%s.%s' % (config.ISSUER_ID,classUid)
    objectUid = "my_loyalty_object_Id_01" # CHANGEME
    # check Reference API for format of "id" (https://developers.google.com/pay/passes/reference/v1/offerobject/insert).
    # Must be alphanumeric characters, '.', '_', or '-'.
    objectId = '%s.%s' % (config.ISSUER_ID,objectUid)
    objectResourcePayload = makeLoyaltyObjectResource(classId, objectId)
    insertOfferObject(objectResourcePayload)

def insertNewLoyaltyClass():
    classUid = "class_id_003"
    classId = '%s.%s' % (config.ISSUER_ID,classUid)
    issuerName = "Zaim Doverie"
    provider = "Qronus"
    programLogoUri = "https://farm66.staticflickr.com/65535/48486234062_d30e5b61f0.jpg"
    programName = "Our Loyalty Program"
    rgbcolor = "#ff01ff"
    classResourcePayload = makeLoyaltyClassResource(classId, issuerName, provider, programLogoUri,programName, rgbcolor)
    insertLoyaltyClass(classResourcePayload)

def makeJwt(objectId):

    signedJwt = None

    try:
        # put into JSON Web Token (JWT) format for Google Pay API for Passes
        googlePassJwt = jwt.googlePassJwt()
        googlePassJwt.addLoyaltyObject({"id": objectId})

        # sign JSON to make signed JWT
        signedJwt = googlePassJwt.generateSignedJwt()
        print(googlePassJwt.__dict__)
        print(googlePassJwt.signer.__dict__)
        print(signedJwt)
    except ValueError as err:
        print(err.args)

    # return "skinny" JWT. Try putting it into save link.
    # See https://developers.google.com/pay/passes/guides/get-started/implementing-the-api/save-to-google-pay#add-link-to-email
    return signedJwt

#insertNewLoyaltyObject()

def createLink():
    classUid = 'class_id_003' # CHANGEME
# check Reference API for format of "id" (https://developers.google.com/pay/passes/reference/v1/offerclass/insert).
# must be alphanumeric characters, '.', '_', or '-'.
    classId = '%s.%s' % (config.ISSUER_ID,classUid)

# your objectUid should be a hash based off of pass metadata. Here we hardcode
    objectUid = 'my_loyalty_object_Id_01' # CHANGEME
# check Reference API for format of "id" (https://developers.google.com/pay/passes/reference/v1/offerobject/insert).
# Must be alphanumeric characters, '.', '_', or '-'.
    objectId = '%s.%s' % (config.ISSUER_ID,objectUid)
    linkJwt = makeJwt(objectId)

    if linkJwt is not None:
        print('This is an "skinny" jwt:\n%s\n' % (linkJwt) )
        print('you can decode it with a tool to see the unsigned JWT representation:\n%s\n' % ('https://developers.google.com/pay/passes/support/testing#test-and-debug-a-jwt') )
        print('Try this save link in your browser:\n%s%s\n' % (config.SAVE_LINK, linkJwt))
        print('this is the shortest type of JWT; recommended for Android intents/redirects\n')

    return

createLink()

if __name__ == '__main__':
    #Note - Is necessary to provide error handling
    pass