from ast import Or
from apps.users.serializers import UserInfoSerializer
from .models import Leave
from .models import User
from rest_framework import serializers

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
class AddLeaveSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Leave
        fields = [
            'id',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'applied_to',
            'created_at',
            'updated_at',
            'users',
            'description',
            'leave_status',
        ]

class LeaveUpdateSerializer(serializers.ModelSerializer): 
    class Meta:  
        model = Leave
        fields = [
            'id',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'applied_to',
            'created_at',
            'updated_at',
            'users',
            'description',
            'leave_status',
        ]
        
class LeaveListSerializer(serializers.ModelSerializer):
    employee_id = UserInfoSerializer()
    user_name = UserInfoSerializer()
    updated_by = UserInfoSerializer()
    class Meta:
        model = Leave
        fields = '__all__'
        depth = 2
        
class LeaveFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'
        depth = 2

