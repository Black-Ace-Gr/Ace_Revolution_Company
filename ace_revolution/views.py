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
        company = request.POST.get("company", "")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name, company=company, email=email, message=message
        )

        # Send email notification
        subject = f"New Contact Message from {name}"
        body = (
            f"Name: {name}\n"
            f"Company: {company or 'N/A'}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ["gregorydavid373@gmail.com"],  # Your email
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully ✅")
        except Exception as e:
            print("Email send error:", e)
            messages.error(request, "Message saved, but email failed to send ❌")

        return redirect("contact")  # your contact page name

    return render(request, "contact.html")
