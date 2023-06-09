from rest_framework import serializers

from mainapp.models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ('number', 'defect')
