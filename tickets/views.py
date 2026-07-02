from rest_framework import viewsets 
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count 


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance._changed_by = self.request.user  # attach user to instance

class DashboardView(APIView):
    def get(self, request):
        total = Ticket.objects.count()
        open_tickets = Ticket.objects.filter(status='open').count()
        inprogress = Ticket.objects.filter(status='in_progress').count()
        resolved = Ticket.objects.filter(status='resolved').count()
        closed = Ticket.objects.filter(status='closed').count()
        highpriority=  Ticket.objects.filter(priority='high').count()
        criticalpriority =  Ticket.objects.filter(priority='critical').count()
        
        
        return Response({
            'total_tickets': total,
            'open': open_tickets,
            'in_progress': inprogress,
            'resolved' : resolved,
            'closed': closed,
            'high_priority': highpriority,
            'critical_priority': criticalpriority,
            
        })