from rest_framework import serializers

from mainapp.models import JobApplication, SparePart, Customer, Department, ScaleModel, Scale, Receiving, Installation


class JobApplicationSerializer(serializers.ModelSerializer):  # список работ
    class Meta:
        model = JobApplication
        fields = "__all__"


class SparePartSerializer(serializers.ModelSerializer):  # список ЗИП
    class Meta:
        model = SparePart
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):  # заказчики
    class Meta:
        model = Customer
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):  # Отделы
    class Meta:
        model = Department
        fields = "__all__"


class ScaleModelSerializer(serializers.ModelSerializer):  # Модели весов
    class Meta:
        model = ScaleModel
        fields = "__all__"


class ScaleSerializer(serializers.ModelSerializer):  # Список весов
    class Meta:
        model = Scale
        fields = "__all__"


class ReceivingSerializer(serializers.ModelSerializer):  # Приход ЗИП
    class Meta:
        model = Receiving
        fields = "__all__"


class InstallationSerializer(serializers.ModelSerializer):  # Установка ЗИП
    class Meta:
        model = Installation
        fields = "__all__"

