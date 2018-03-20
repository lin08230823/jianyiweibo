
from django.urls import path
from .views import homepage,user_page,wb_update,wb_comment,wb_forward
app_name = 'weibo'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('u',user_page, name='upage'),
    path('update',wb_update, name='update'),
    path('comment',wb_comment, name='comment'),
    path('forward',wb_forward, name='forward')
]
