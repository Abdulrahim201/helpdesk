from django.db import models
from django.contrib.auth.models import User


class Priority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'
    CRITICAL= 'critical' , 'Critical'

class Status(models.TextChoices):
    OPEN = 'open' , 'Open'
    IN_PROGRESS = 'in_progress' , 'In_progress'
    RESOLVED = 'resolved' , 'Resolved'
    CLOSED = 'closed' , 'Closed'

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TicketHistory(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='history' )
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='changed_tickets')
    changed_at = models.DateTimeField(auto_now=True)
    field_changed = models.CharField(max_length=50)
    old_value =  models.TextField()
    new_value =  models.TextField()
    
    class Meta:
        ordering = ['-changed_at']

    def __str__(self):
        return f"{self.field_changed} changed on Ticket #{self.ticket.id}"