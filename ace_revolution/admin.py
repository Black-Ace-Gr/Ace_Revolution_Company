from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "date_sent")
    search_fields = ("name", "email", "company")
    list_filter = ("date_sent",)
