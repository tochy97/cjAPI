from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, "cjAPI/templates/index.html", {})
