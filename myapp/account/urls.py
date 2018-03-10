from django.urls import path
from .views import register,log_out,log_in
app_name = 'account'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout')
]
