from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def mainmenu(request):
    return render(request, 'mainmenu.html')

def contactus(request):
    return render(request, 'contactus.html')

def submissioncomplete(request):
    return render(request, 'submissioncomplete.html')