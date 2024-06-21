from django.urls import path
from .views import home,tweet_create,tweet_delete,tweet_edit,register,logout_view
urlpatterns = [
    path('',home,name='home'),
    path('create/',tweet_create,name='create'),
    path('edit/<int:pk>/',tweet_edit,name='edit'),
    path('delete/<int:pk>/',tweet_delete,name='delete'),
    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout'),

]