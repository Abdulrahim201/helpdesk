from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, DashboardView
from django.urls import path

router = DefaultRouter()
router.register(r'tickets',TicketViewSet, basename='ticket')

urlpatterns = router.urls + [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
