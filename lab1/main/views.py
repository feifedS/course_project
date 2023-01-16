from django.shortcuts import render

# Create your views here.
def index(request):
    print("HELLO")

    return render(request, 'main/index.html')

def auth(request):
    print("Логин: ", request.POST.get("login"))
    print("Пароль: ", request.POST.get("password"))

def registration(request):
    pass