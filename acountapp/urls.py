from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from acountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = 'acountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='acountapp/login.html'),
         name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail')
]