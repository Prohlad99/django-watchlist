from django.urls import path
from . import models
from . import views

urlpatterns = [
    path('', views.WatchList.as_view(), name='watchlist'),
    path('<int:pk>/', views.WatchListDetail.as_view(), name='watchlist_detail'),
    path('platform/', views.PlatformList.as_view(), name='platforms'),
    path('platform/<int:pk>/', views.PlatformDetail.as_view(), name='platform_detail'),
   
]