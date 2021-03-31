from django.contrib import admin
from .models import Chat, Message, Contact

admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
