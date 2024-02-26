from rest_framework import serializers
from book.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','price']

class UserSerializer(serializers.ModelSerializer):
        password=serializers.CharField(write_only=True)


        class Meta:
            model=User
            fields=['id','username','password']

        def create(self, validated_data):
            u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
            u.save()
            return u


