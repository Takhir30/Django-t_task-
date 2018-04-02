from django import forms


class FormappForm(forms.Form):
    name = forms.CharField(max_length=50)
