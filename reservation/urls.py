from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("mainmenu", views.mainmenu, name="mainmenu"),
    path("contactus", views.contactus, name="contactus"),
    path("submissioncomplete", views.submissioncomplete, name="submissioncomplete"),
]