from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
        #x = (str("mon/"+months[month-1]))
        redirect_path = reverse("month-challenge", args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Month not found!!!")


def monthly_challenge(requst, month):
    try:
        return(HttpResponse(challenge_months[month]))
    except:
        return HttpResponseNotFound("No month found !!!")
