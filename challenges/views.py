from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
challenge_months = {
    "jan": "This is Jan!!!",
    "feb": "This is Feb!!!",
    "mar": "This is Mar!!!",
    "apr": "This is Apr!!!",
    "may": "This is May!!!",
    "jun": "This is June!!!",
}


def index(request):
    return HttpResponse("This works!!")


def monthly_challenge_number(request, month):
    return HttpResponse(month)


def monthly_challenge(requst, month):
    try:
        return(HttpResponse(challenge_months[month]))
    except:
        return HttpResponseNotFound("No month found !!!")
