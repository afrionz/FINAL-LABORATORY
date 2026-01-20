from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Facility(models.Model):
    FACILITY_STATUS = [
        ('Available', 'Available'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Closed', 'Closed'),
    ]

    facility_name = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=FACILITY_STATUS,
        default='Available'
    )
    def __str__(self):
        return self.facility_name

class Reservation(models.Model):
    RESERVATION_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    facility = models.ForeignKey( Facility,on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    date_reserved = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=RESERVATION_STATUS,
        default='Pending'
    )

    def __str__(self):
        return f"{self.facility} - {self.date_reserved}"

    def get_absolute_url(self):
        return reverse(
            viewname='reservation_detail',
            kwargs={'pk': self.pk}
        )

    def get_success_url(self):
        return reverse_lazy('home')


class MaintenanceRequest(models.Model):
    PRIORITY_LEVEL = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    MAINTENANCE_STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE
    )
    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    issue_description = models.TextField()
    date_reported = models.DateField(auto_now_add=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_LEVEL
    )
    status = models.CharField(
        max_length=15,
        choices=MAINTENANCE_STATUS,
        default='Pending'
    )

    def __str__(self):
        return f"{self.facility} - {self.status} - {self.date_reported}"


class MaintenanceWorkOrder(models.Model):
    maintenance_request = models.ForeignKey(
        MaintenanceRequest,
        on_delete=models.CASCADE
    )
    assigned_staff = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    work_details = models.TextField()
    date_started = models.DateField()
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Work Order #{self.pk}"