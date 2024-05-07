from django import forms

class InputForm(forms.Form):
    upc = forms.CharField(label='Enter UPC')
