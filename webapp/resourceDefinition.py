def makeLoyaltyClassResource(classId, issuerName, provider, programLogoUri, programName, rgbcolor):
  # Define the resource representation of the Class
  # values should be from your DB/services; here we hardcode information

    payload = {}

  # below defines an offer class. For more properties, check:
  # https://developers.google.com/pay/passes/reference/v1/offerclass/insert
  # https://developers.google.com/pay/passes/guides/pass-verticals/offers/design

    payload = {
    # required fields
    "id" : classId
    ,"issuerName" : issuerName
    ,"provider" : provider
    ,"programLogo" : {
        'kind': 'walletobjects#image',
        'sourceUri': {
            'kind': 'walletobjects#uri',
            'uri': programLogoUri
            }
        }
    ,"programName" : programName
    ,"reviewStatus" : "underReview"
    
    # optional.  Check design and reference api to decide what's desirable
    , "hexBackgroundColor" : rgbcolor
    }
    
    return payload
