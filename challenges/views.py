from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("This works!!")


def monthly_challenge(requst, month):
    if month == "jan":
        challenge_text = "This is Jan!!!"
    elif month == "feb":
        challenge_text = "This is Feb!!!"
    elif month == "mar":
        challenge_text = "This is Mar!!!"
    elif month == "apr":
        challenge_text = "This is April!!!"
    elif month == "may":
        challenge_text = "This is May!!!"
    else:
        return HttpResponseNotFound("Not available!!!")
    return(HttpResponse(challenge_text))
    