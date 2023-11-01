from rest_framework import serializers
from crm.models import Students

class StudentSerailizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Students
        # exclude=("id",)
        fields="__all__"  