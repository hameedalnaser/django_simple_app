from django import forms

class InputFrom(forms.Form):
    x = forms.IntegerField(label="Enter x")
    y = forms.IntegerField(label="Enter y")
    