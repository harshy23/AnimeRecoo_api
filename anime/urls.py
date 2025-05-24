from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.new_user,name="new_user"),
    path("search/",views.anime_search,name="anime_search"),
    path("recommendations/",views.anime_recommendation,name="anime_recommendation"),
    path("preferences/",views.user_preference_genre,name="user_preference_genre"),
    
    # Add your app's URL patterns here
]