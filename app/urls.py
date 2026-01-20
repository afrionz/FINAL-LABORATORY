from django.urls import path, include
from .views import (
    HomePageView,
    AboutPageView,
    FacilityListView,
    FacilityDetailView,
    ReservationCreateView,
    MaintenanceRequestCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('facilities/', FacilityListView.as_view(), name='facility_list'),
    path('facility/<int:pk>/', FacilityDetailView.as_view(), name='facility_detail'),

    path('reserve/', ReservationCreateView.as_view(), name='reservation_create'),
    path('maintenance/', MaintenanceRequestCreateView.as_view(), name='maintenance_create'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]