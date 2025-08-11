from django.contrib import admin
from .models import Job

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'verified', 'expiry_date', 'posted_at')
    list_filter = ('verified', 'location', 'company')
    search_fields = ('title', 'company', 'location')
    readonly_fields = ('posted_at',)