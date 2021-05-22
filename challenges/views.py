from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    try:
        months = list(challenge_months.keys())
        return HttpResponseRedirect(months[month-1])
    except:
        return HttpResponseNotFound("Month not foung!!!")


def monthly_challenge(requst, month):
    try:
        return(HttpResponse(challenge_months[month]))
    except:
        return HttpResponseNotFound("No month found !!!")
