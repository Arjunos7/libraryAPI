from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from book.models import Book
from book.serializers import BookSerializer
from book.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets

# class Bookrecords(APIView):
#     def get(self,request):
#         books=Book.objects.all()
#         b=BookSerializer(books,many=True)
#         return Response(b.data)
#
#     def post(self,request):
#         b=BookSerializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)



'''mixins based'''
# class Bookrecords(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):   #non primarykey based
#     queryset=Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self,request):
#          return self.list(request)
#
#     def post(self,request):
#         return self.create(request)



'''mixins based'''
# class Bookdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self,request,pk):
#          return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request,pk)
#
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

'''generics based'''

# class Bookrecords(generics.ListCreateAPIView):     #non primary key based
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class Bookdetails(generics.RetrieveUpdateDestroyAPIView):    #primary key based
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

'''viewsets'''

class Bookrecords(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Book.objects.all()
    serializer_class=BookSerializer







class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer






