from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .serializers import JobApplicationSerializer, SparePartSerializer, CustomerSerializer, DepartmentSerializer, \
    ScaleModelSerializer, ScaleSerializer, ReceivingSerializer, InstallationSerializer
from .models import JobApplication, SparePart, Customer, Department, ScaleModel, Scale, Receiving, Installation


class JobViewSet(viewsets.ModelViewSet):  # список работ
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = (IsAdminUser, )


class SparePartViewSet(viewsets.ModelViewSet):  # список ЗИП
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CustomerViewSet(viewsets.ModelViewSet):  # заказчики
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DepartmentViewSet(viewsets.ModelViewSet):  # Отделы
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ScaleModelViewSet(viewsets.ModelViewSet):  # Модели весов
    queryset = ScaleModel.objects.all()
    serializer_class = ScaleModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ScaleViewSet(viewsets.ModelViewSet):  # Список весов
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ReceivingViewSet(viewsets.ModelViewSet):  # Приход ЗИП
    queryset = Receiving.objects.all()
    serializer_class = ReceivingSerializer
    permission_classes = (IsAdminUser, )


class InstallationViewSet(viewsets.ModelViewSet):  # Установка ЗИП
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer
    permission_classes = (IsAdminUser, )


# class JobAPIView(generics.ListCreateAPIView):  # заявки в работу
#     queryset = JobApplication.objects.all()
#     serializer_class = JobApplicationSerializer
#
#
# class JobAPIUpdate(generics.UpdateAPIView):  # заявки в работу
#     queryset = JobApplication.objects.all()
#     serializer_class = JobApplicationSerializer
#
#
# class JobAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # заявки в работу
#     queryset = JobApplication.objects.all()
#     serializer_class = JobApplicationSerializer
#
#
# class SparePartAPIView(generics.ListCreateAPIView):  # запчасти с артикулами
#     queryset = SparePart.objects.all()
#     serializer_class = SparePartSerializer
#
#
# class SparePartAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # запчасти с артикулами
#     queryset = SparePart.objects.all()
#     serializer_class = SparePartSerializer
