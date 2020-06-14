from rest_framework import serializers
from .models import Leave


class LeaveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['start_date', 'end_date', 'start_time', 'end_time']


class LeaveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['is_accepted', 'comment']


class LeaveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['id', 'applicant', 'start_date', 'end_date', 'start_time', 'end_time', 'is_accepted', 'comment']
