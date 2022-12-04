from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Tweet,User
from .serializer import TweetSerializer,UserSerializer
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def index(request):

        if request.method=='GET':
            q=request.GET.get('q')

            if q != None:
                tweets= Tweet.objects.filter(Q(desc__icontains=q))
                serializer= TweetSerializer(tweets, many=True)
                return Response(serializer.data)
                
            tweets= Tweet.objects.all()
            serializer= TweetSerializer(tweets, many=True)
            return Response(serializer.data)

        if request.method=='POST':
            serializer = TweetSerializer(data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def findUser(request,username):
    
    # users=User.objects.get(username=username)
    user=User.objects.get(username=username)
    if request.method=='GET':
        serializer= UserSerializer(user, many=False)
        return Response(serializer.data)
    
    if request.method=='PUT':   
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def users(request):
    if request.method=='GET':
        users= User.objects.all()
        serializer= UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer = UserSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    


