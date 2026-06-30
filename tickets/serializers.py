from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'created_by', 'assigned_to']
        read_only_fields = ['created_at', 'updated_at']