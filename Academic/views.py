from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
from MyUni import settings


def contact_form(request):
    return render(request, "contactForm.html")


def contact(request):
    if request.method == "POST":
        subject = request.POST["txtSubject"]
        message = request.POST["txtMessage"] + " / Email: " + request.POST["txtEmail"]
        email_from = settings.EMAIL_HOST_USER
        email_for = ["email_example@gmial.com"]
        send_mail(subject, message, email_from, email_for, fail_silently=False)
        return render(request, "successContact.html")
    return render(request, "contactForm.html")

