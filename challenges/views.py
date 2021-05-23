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
    response_data = "<h2>Following are the months</h2>\n<br>\n"
    months = list(challenge_months.keys())
    for month in months:
        link = reverse("month-challenge",args=[month])
        response_data += f'<a href="{link}">Click Here for {month.capitalize()}</a>\n<br>\n'
    return HttpResponse(response_data)


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
        respose_data = f"<h1>{challenge_months[month]}</h1>"
        return HttpResponse(respose_data)
    except:
        return HttpResponseNotFound("No month found !!!")
