from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        is_exist = User.objects.filter(username=username)
        if password == password2 and not is_exist:
            user = WBUser