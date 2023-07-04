# forms.py
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    message = forms.CharField(widget = forms.Textarea )

# class JournalItemForm(forms.Form):
#     account = forms.CharField(label='Account', max_length=100)
#     description = forms.CharField(label='Description', max_length=100)
#     contact = forms.CharField(label='Contact (INR)', max_length=100)
#     debits = forms.DecimalField(label='Debits')
#     credits = forms.DecimalField(label='Credits')