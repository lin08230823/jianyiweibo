from django.shortcuts import render
from app.models import WBUser
def index(request):
    users = WBUser.objects.all().order_by('-id')[:10]
    return render(request, 'index.html',{
        'users': users
    })
