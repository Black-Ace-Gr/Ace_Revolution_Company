from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


# Create your views here.

def home(request):
    return render(request, "ace_revolution/home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company = request.POST.get("company")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            company=company,
            email=email,
            message=message
        )

        # Optionally send an email notification
        try:
            send_mail(
                subject=f"New Contact from {name}",
                message=f"Company: {company}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email failed: {e}")

        return render(request, "ace_revolution/email_sent.html", {"name": name})

    return render(request, "ace_revolution/email_sent.html")
