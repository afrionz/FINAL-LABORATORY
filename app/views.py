from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Facility, Reservation, MaintenanceRequest


class HomePageView(TemplateView):
    template_name = 'app/home.html'
class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class FacilityListView(ListView):
    model = Facility
    context_object_name = 'facilities'
    template_name = 'app/facility_list.html'

class FacilityDetailView(DetailView):
    model = Facility
    context_object_name = 'facility'
    template_name = 'app/facility_detail.html'

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ['facility','purpose','date_reserved','start_time','end_time']
    template_name = 'app/reservation_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MaintenanceRequestCreateView(CreateView):
    model = MaintenanceRequest
    fields = ['facility','issue_description','priority']
    template_name = 'app/maintenance_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        return super().form_valid(form)