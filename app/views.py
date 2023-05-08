from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import detail


def index(request):
    """
    A simple view function to take user data and send email to the user's email id and render the template
    index.html
    :param request: user request
    :return: render index.html template
    """
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = detail(name=name, email=email, subject=subject, message=message)
        ins.save()
        """
        Send email to user
        """
        subject = 'Thank you for contacting'
        message = f'Hi {name},\n\nI received your message.\nThank you for contacting me.'
        from_email = 'radhikapiplani12@gmail.com'  # Replace with your email address
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        """
        Add success message to Django messages
        """
        messages.success(request, 'Form submitted successfully!')
        """
        Redirect to the same view after successful form submission
        """
        return redirect('index')
    else:
        return render(request, 'index.html')
