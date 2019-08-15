#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from webapp.restapi import getLoyaltyClassList, getLoyaltyObjectList

# from webapp.weather import weather_by_city
# from webapp.python_org_news import get_python_news
from dotenv import load_dotenv
import json

def create_app():

    app = Flask (__name__)
    load_dotenv()

    @app.route('/')
    def index():
        # title = "Новости Python"
        # weather = weather_by_city("Vladivostok, Russia")
        loyaltyClassList = getLoyaltyClassList()
        json_data_classes = json.loads(loyaltyClassList.text)
        loyaltyObjectList = getLoyaltyObjectList()
        json_data_objects = json.loads(loyaltyObjectList.text)
        # news_list = get_python_news()
        # typeofobj = type(loyaltyClassList)
        # print(typeofobj)
        # print(json_data)
        return render_template("index.html",loyaltyClassList = json_data_classes['resources'],loyaltyObjectList = json_data_objects['resources'], )

    return app
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)