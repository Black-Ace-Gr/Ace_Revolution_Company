from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import ContactMessage


# Create your views here.

def home(request):
    return render(request, "ace_revolution/home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            telephone = telephone,
            subject=subject,
            message=message
        )

        messages.success(request, "Message received! I’ll get back to you soon.")
        return redirect("contact")

    return render(request, "ace_revolution_company/contact.html")