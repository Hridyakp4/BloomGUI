from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):

    cls = joblib.load('text_classification.joblib')

    text =[0]
    text[0] = request.GET['Sentence']
    ans = cls.predict(text)
    return render(request, "result.html", {'ans': ans[0]})
