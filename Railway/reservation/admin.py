from django.contrib import admin
from .models import trains,person

@admin.register(trains)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['id','train_name', 'source', 'destination', 'time','price','seats_available']

@admin.register(person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','gender','email','date_and_time_of_booking','train']