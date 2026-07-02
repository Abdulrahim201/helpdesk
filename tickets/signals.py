from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Ticket, TicketHistory

@receiver(pre_save, sender=Ticket)
def log_ticket_changes(sender, instance, **kwargs):
    print(f"Signal fired for ticket: {instance.pk}")
    if instance.pk:  # only if ticket already exists
        try:
            old_ticket = Ticket.objects.get(pk=instance.pk)
            fields_to_track = ['title', 'description', 'priority', 'status', 'assigned_to']
            
            for field in fields_to_track:
                old_value = str(getattr(old_ticket, field))
                new_value = str(getattr(instance, field))
                
                if old_value != new_value:
                    TicketHistory.objects.create(
                        ticket=instance,
                        changed_by=getattr(instance, '_changed_by', None),  # use attached user
                        field_changed=field,
                        old_value=old_value,
                        new_value=new_value
                    )
        except Ticket.DoesNotExist:
            pass