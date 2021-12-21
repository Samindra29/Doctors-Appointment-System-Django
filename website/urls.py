from django.urls import path
from . import views  
from .views import AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', views.home, name="home"),
    # path('appointment.html', views.appointment, name="appointment"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path('manage_app.html', views.manage_app, name="manage_app"),
    path('appointment_succ.html', views.appointment_succ, name="appointment_succ"),
    path('contact_us.html', views.contact_us, name="contact_us"),
    path("manage-appointment/", ManageAppointmentTemplateView.as_view(), name="manage_app"),
]

