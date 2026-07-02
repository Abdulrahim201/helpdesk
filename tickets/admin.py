from django.contrib import admin
from .models import Ticket
from .models import TicketHistory
# Register your models here.

class TicketHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ['ticket', 'changed_by', 'changed_at', 'field_changed', 'old_value', 'new_value']
    def has_add_permission(self, request):
        return False  # nobody can manually add history
    
    def has_change_permission(self, request, obj=None):
        return False  # nobody can edit history
    
class TicketAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj._changed_by = request.user  # attach the logged in user
        super().save_model(request, obj, form, change)

admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketHistory,TicketHistoryAdmin)