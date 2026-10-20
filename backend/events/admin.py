
from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "venue")
    search_fields = ("title", "venue")
    list_filter = ("date",)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "email",
        "event_name",
        "created_at",
    )
    search_fields = ("student_name", "email")
    list_filter = ("event_name",)