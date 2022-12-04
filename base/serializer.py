from rest_framework import serializers
from .models import Tweet,User



class UserSerializer(serializers.ModelSerializer):
    tweet_count=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=['email','username','name','tweet_count']
# has to start from get
    def get_tweet_count(self, obj):
        user=User.objects.get(name=obj)
        users_tweet=Tweet.objects.filter(user=user)
        count= users_tweet.count()
        return count


class TweetSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model= Tweet
        fields= ['desc','created','likes', 'user']


