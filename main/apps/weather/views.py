from django.shortcuts import render, redirect
from django.contrib import messages, sessions

# views fo login


def index(request):
    if "location1" not in request.session:
        request.session['location1'] = 'New York'
    if "location2" not in request.session:
        request.session['location2'] = 'Chicago'
    if "location3" not in request.session:
        request.session['location3'] = 'San Francisco'
    if "location4" not in request.session:
        request.session['location4'] = 'Washington D.C'
    return render(request, "html/index.html")


def newLocation1(request):
    request.session['location1'] = request.POST["location1"]
    return redirect("/")

def newLocation2(request):
    request.session['location2'] = request.POST["location2"]
    return redirect("/")

def newLocation3(request):
    request.session['location3'] = request.POST["location3"]
    return redirect("/")

def newLocation4(request):
    request.session['location4'] = request.POST["location4"]
    return redirect("/")
