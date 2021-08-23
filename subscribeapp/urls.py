from django.urls import path

from subscribeapp.views import SubscriptionView, SubscribeListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscribeListView.as_view(), name='list'),

]