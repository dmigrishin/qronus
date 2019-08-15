#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def updateLoyaltyObjectResource(classId, objectId):
    payload = {}
    payload = {
        # required fields
        "id" : objectId
        ,"classId" : classId
        ,"state" : "active"
        # optional.  Check design and reference api to decide what's desirable
        ,"loyaltyPoints": {
            "balance": {
                "string": "900",
                
            }
        }
        ,"version":"2"
    }
    return payload

def makeLoyaltyObjectResource(classId, objectId):
  # Define the resource representation of the Object
  # values should be from your DB/services; here we hardcode information

    payload = {}
    

    # below defines an offer object. For more properties, check:
    # https://developers.google.com/pay/passes/reference/v1/offerobject/insert
    # https://developers.google.com/pay/passes/guides/pass-verticals/offers/design

    payload = {
        # required fields
        "id" : objectId
        ,"classId" : classId
        ,"state" : "active"
        # optional.  Check design and reference api to decide what's desirable
        ,"barcode": {
            "type": "qrCode"  #check reference API for types of barcode
            ,"value": "1234abc"
            ,"alternateText": "Ну Привет"
        }
        ,"loyaltyPoints": {
            "label": "Points Balance",
            "balance": {
                "string": "500",
                
            }
        }
    }

    return payload
