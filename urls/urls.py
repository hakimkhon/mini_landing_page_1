from operator import concat
from django.urls import path
from .views import *

app_name = "urls"

urlpatterns = [
    path('', Home, name="Home"),
    path('contact', Contact, name="Contact"),
    path('privacy', Privacy, name="Privacy"),
    path('Report-Malicious-URL', Report_Malicious_URL, name="Report"),
    path('URL-Click-Counter', URL_Click_Counter, name="URL"),
    path('Terms-of-Service', Terms_of_Service, name="Terms"),
    path('test', test, name="test"),
]