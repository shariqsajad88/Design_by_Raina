
# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

def homepage(request):
    if request.method == 'POST':
        # Get form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Create the email content
        email_subject = f"New Message from {name} - {service}"
        email_message = f"""
        You have received a new message from {name}.

        Contact Information:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Service: {service}

        Message:
        {message}
        """
        # Send the email
        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,  # Default sender email
                ['admin@example.com'],  # Admin email (you can customize this)
            )

            # Return a success response
            return JsonResponse({'message': 'Thank you for your message! We will get back to you soon.'}, status=200)
        except Exception as e:
            # Return an error response if the email fails to send
            return JsonResponse({'message': f'Something went wrong. Please try again. Error: {str(e)}'}, status=500)
    
    # If it's a GET request, render the homepage
    return render(request, 'home/index.html')
