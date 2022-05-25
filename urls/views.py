from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, "home.html")

def Contact(request):
    return render(request, "base/Contact.html")

def Privacy(request):
    return render(request, "base/Privacy.html")

def Report_Malicious_URL(request):
    return render(request, "base/Report_Malicious_URL.html")

def URL_Click_Counter(request):
    return render(request, "base/URL_Click_Counter.html")

def Terms_of_Service(request):
    return render(request, "base/Terms_of_Service.html")

def test(request):
    return render(request, "others/test.html")
