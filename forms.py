from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    phone = forms.CharField(max_length=14, required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
