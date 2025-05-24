from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .anilist import anime_by_genre,anime_by_name,anime_by_recommendations
from .models import Useranime
from .serializers import useranime
import json

@api_view(['POST'])
def new_user(request):
    User = get_user_model()
    if request.methos=="POST":
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username = name).exists():
            return Response({"error":"Name Already exitst"},status=400)
        elif User.objects.filter(email = email).exista():
            return Response({"error":"Email already used"},status=400)
        else:
            user = User.objects.create_user(username = name , email = email , password = password)
            user.save()

            return Response({"message":"user created"},status =201)
    else:
        return Response({"error":"Invalid REquest method"},status=405)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def anime_search(request):
    name = request.query_params.get("name")
    genre =request.query_params.get("genre")

    if name:
       return Response(anime_by_name(name))
    elif genre:
        return Response(anime_by_genre(genre))
    else:
        return Response({"error":"give name or select any genre"})
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_preference_genre(request):
    user = request.user
    pref, created = Useranime.objects.get_or_create(user=user)

    if request.method == 'GET':

        return Response({"user_genre": json.loads(pref.favgenres)})
    
    elif request.method == 'POST':
        genres = request.data.get('user_genre',[])

        if not isinstance(genres,list):
            return Response({"error":"user_genre must be a list"})
        
        pref.favgenres = json.dumps(genres)
        pref.save()

        return Response({"message":"user_pref saved","user_pref" : json.loads(pref.favgenres)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def anime_recommendation(request):

    user = request.user
    try:
        pref = Useranime.objects.get(user=user)

    except Useranime.DoesNotExist:
        return Response({"error":"user_geners are notpresnt"},status=404)
    return Response(anime_by_recommendations(json.loads(pref.favgenres)))


# Create your views here.
