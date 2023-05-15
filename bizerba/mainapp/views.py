from django.shortcuts import render
from rest_framework import generics
from .serializers import JobApplicationSerializer
from .models import *


class JobAPIView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
