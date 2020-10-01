from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"New contact form message from: {form.cleaned_data['name']}"
            from_email = form.cleaned_data['from_email']
            message = f"Name: {form.cleaned_data['name']}\nPhone: {form.cleaned_data['phone']}\n" \
                      f"Email: {form.cleaned_data['from_email']}\nMessage: {form.cleaned_data['message']}"
            try:
                send_mail(subject, message, from_email, ['denise@decaforklift.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success_view(request):
    return render(request, "success.html")
