from unittest import TestCase

from .models import Appointment

# Create your tests here.

data = dict(
    fname= 'test',
    lname = 'user' ,
    email = 'testUser@mail',
    mob = 232,
    ans = 'need assistance'  # message request
)

def post(data):
    fname = data['fname']
    lname = data['lname'] 
    email = data['email']
    mob = data['mob']
    ans = data['ans']  # message request

    appointment = Appointment.objects.create(
        fname = fname,
        lname = lname,
        email = email,
        phone = mob,
        request = ans,
    )
    return appointment


class test_AppointmentTemplateView(TestCase):

    def test_post(self):
        result = post(data)
        assert result.__dict__.values(), data.values()
