from rest_framework import serializers
from .models import trains, person

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = trains
        fields = ['train_name', 'source', 'destination', 'time','price','seats_available']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = ['name','age','gender','email','date_and_time_of_booking','train']