from django.contrib import admin
from .models import Car, CarUser, UserTest

# Register your models here.
admin.site.register(Car)
admin.site.register(CarUser)
admin.site.register(UserTest)
