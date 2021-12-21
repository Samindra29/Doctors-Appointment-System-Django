# will send context to all pages.
# like a global view.

from .models import Appointment

def notification_bell(request):
    count = Appointment.objects.filter(accepted= False).count()
    bell = {
        "count": count
    }
    return bell