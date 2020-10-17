from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LibUser)
admin.site.register(LibBook)
admin.site.register(LibCategory)
admin.site.register(LibBookAcquired)