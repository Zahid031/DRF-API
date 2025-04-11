from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    members_count=serializers.IntegerField(read_only=True)
    members=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='profile-detail',source='members')
    manager=serializers.HyperlinkedRelatedField(read_only=True, view_name='profile-detail')
    class Meta:
        model=House
        fields=['url','id','name','image','created_on','description','manager','members_count','members','points','completed_tasks_count','pending_tasks_count']
        read_only_fields=['created_on','points','completed_tasks_count','pending_tasks_count']