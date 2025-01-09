from django.urls import path
from . import models
from . import views

urlpatterns = [
    path('', views.WatchList.as_view(), name='watchlist'),
    path('<int:pk>/', views.WatchListDetail.as_view(), name='watchlist_detail'),
    path('platform/', views.PlatformList.as_view(), name='platforms'),
    path('platform/<int:pk>/', views.PlatformDetail.as_view(), name='platform_detail'),
    # path('review/', views.ReviewList.as_view(), name='review'),
    # path('review/<int:pk>/', views.ReviewDetails.as_view(), name='review_detail'),

    path('<int:pk>/review/create', views.ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/review/', views.ReviewList.as_view(), name='review'),
    path('<int:pk>/review/<int:review_pk>/', views.ReviewDetails.as_view(), name='review_detail'),


   
]