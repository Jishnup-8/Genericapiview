from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from . models import Student
from . serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.filters import SearchFilter,OrderingFilter

class StudentListCreateAPIView(ListAPIView):
    authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]

    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    filter_backends =[SearchFilter,OrderingFilter]
    search_fields =['^name']
    Ordering_filter =['name']

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
