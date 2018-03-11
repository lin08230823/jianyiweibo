
from django.urls import path
from .views import homepage,user_page
app_name = 'weibo'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('u',user_page, name='upage')
]
