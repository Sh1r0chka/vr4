from django.contrib import admin
from .models import *

admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(CustomUser)


