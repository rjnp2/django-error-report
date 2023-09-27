from django.contrib import admin

from error_report.models import ErrorDetail


@admin.register(ErrorDetail)
class ErrorDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'error_type', 'info', 'error_occured_at')
    list_display_links = ('id', 'path', 'error_type', 'info', 'error_occured_at')
    ordering = ('-id',)
    search_fields = ('path', 'error_type', 'info', 'data')

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

