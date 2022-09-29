from django.contrib import admin
from .models import Score
# Register your models here.

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ['name', 'score']


# admin.site.register(Message, MessageAdmin)
admin.site.register(Score)