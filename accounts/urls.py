
from django.urls import path
from . views import StudentListCreateAPIView,StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
   path('students/', StudentListCreateAPIView.as_view()),
   path('students/<int:pk>/' ,StudentRetrieveUpdateDestroyAPIView.as_view()),
]