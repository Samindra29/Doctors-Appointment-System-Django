from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import Settings
from django.core.mail import EmailMessage, message
from django.core.mail import send_mail     # for the sending email funtionality
from django.conf import ENVIRONMENT_VARIABLE, settings
from .models import Appointment
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.http.response import HttpResponseRedirect
import datetime
from django.template import Context
from django.template.loader import get_template


def home(request):
    return render(request, 'home.html', {})

# def appointment(request):
#     #return render(request, 'appointment.html')
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname'] 
#         email = request.POST['email']
#         mob = request.POST['mob']
#         app_time = request.POST['app_time']
#         app_day = request.POST['app_day']
#         ans = request.POST['ans']

#         email = EmailMessage(
#             subject= "Appointment request received",
#             body= f"{fname} {lname}, we have  received your request for {app_day} {app_time}. We will confirm you soon through your email: {email} or mobile: {mob}. Thank you",
#             from_email=settings.EMAIL_HOST_USER,
#             to=[settings.EMAIL_HOST_USER],
#             reply_to=[email]
#         )
#         email.send()

#         appointment = Appointment.objects.create(
#             fname = fname,
#             lname = lname,
#             email = email,
#             phone = mob,
#             req_time = app_day,
#             req_time = app_time,
#             request = ans,
#         )
#         appointment.save()
        
#         return render(request, 'appointment_succ.html', {'name': fname ,'app_time' : app_time , 'app_day' : app_day})
#     else:
#         return render(request, 'appointment.html')

class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname'] 
        email = request.POST['email']
        mob = request.POST['mob']
        ans = request.POST['ans']  # message request

        appointment = Appointment.objects.create(
            fname = fname,
            lname = lname,
            email = email,
            phone = mob,
            request = ans,
        )
        appointment.save()

        messages.add_message(request,messages.SUCCESS, f"thank you {fname} {lname}. We will confirm you your apointment through your email: {email} soon!")
        return HttpResponseRedirect(request.path)



def manage_app(request):
    return render(request, 'manage_app.html', {})



def contact_us(request):
    # this is the contact us form in the bottom of home
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            email,
            message,
            name,
            ['medicareunited2021@gmail.com'],
        )
        # return render(request, 'contact_us.html')
        messages.add_message(request, messages.SUCCESS, f"Dear {name}, your request has been sent to us, we will get back to you through your email: '{email}' soon.")
        return HttpResponseRedirect(request.path)

    else:
        return render(request, 'contact_us.html', {})

       

def appointment_succ(request):
    return render(request, 'appointment_succ.html', {})



class ManageAppointmentTemplateView(TemplateView):
    template_name = "manage_app.html"
    model = Appointment
    login_required = True   # so not everyone can access the manage page
    
    def post(self, request):
        date= request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id= appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        info = {
            "fname" : appointment.fname,
            "lname" : appointment.lname,
            "date" : date,
        }
        message = get_template('email.html').render(info)

        email= EmailMessage(
            "Appointment confirmation at Medicare United Hospital",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype= "html"
        email.send()


        messages.add_message(request, messages.SUCCESS, f"Patient {appointment.fname}'s appointment has been set for {date}")
        return HttpResponseRedirect(request.path)



    # in order to send some extra data form the template to the view we write get_context_data ()
    def get_context_data(self, *args, **kwargs):   
        context= super().get_context_data(*args, **kwargs)
        appointment= Appointment.objects.all()

        context.update({
            "appointment" : appointment,
            "title" : "Manage Appointments"
        })
        return context










        
        
