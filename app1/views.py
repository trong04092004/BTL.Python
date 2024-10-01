from django.shortcuts import render

# Create your views here.
def home(reqest):
    return render(reqest,'app1/home.html')
def base(reqest):
    return render(reqest,'app1/base.html')

