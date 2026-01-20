from django.contrib import admin
from .models import (
    Department,
    Facility,
    Reservation,
    MaintenanceRequest,
    MaintenanceWorkOrder
)

admin.site.register(Department)
admin.site.register(Facility)
admin.site.register(Reservation)
admin.site.register(MaintenanceRequest)
admin.site.register(MaintenanceWorkOrder)