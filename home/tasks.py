from __future__ import absolute_import
from celery import shared_task
import requests
import json

@shared_task
def send(number,zipcode):
    weatherResponse = requests.get("http://api.wunderground.com/api/7c95bc3797fb35f1/forecast/q/"+zipcode+".json")
    weatherObject = json.loads(weatherResponse.text)
    message ="\n" + "\n" + "\n" + weatherObject["forecast"]["txt_forecast"]["forecastday"][0]["title"]
    message += "\n" + weatherObject["forecast"]["txt_forecast"]["forecastday"][0]["fcttext"]
    sms = {'number':number,'message':message}
    result = requests.post("http://textbelt.com/text",data=sms)
    print result.text