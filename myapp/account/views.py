from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from app.models import WBUser
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        is_exist = User.objects.filter(username=username)
        if password == password2 and not is_exist:
            user = WBUser.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            login(request, user)
            return redirect('wb:homepage')
        else:
            return HttpResponse('密码不一致或用户名已存在')
    else:
        return redirect('/')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return redirect('wb:homepage')
        else:
            return HttpResponse('密码错误或用户不存在')
    else:
        return redirect('/')

def log_out(request):
    logout(request)
    return redirect('/')