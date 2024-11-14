from django import forms

class StudForm(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student name')
    s_aadhar = forms.CharField(max_length=30,label='Aaadhar Number')
    s_class = forms.CharField(max_length=30,label='Class')
    s_division = forms.CharField(max_length=30,label='Division')
    s_egrantid = forms.CharField(max_length=30,label='E-grant ID')
    s_category = forms.CharField(max_length=30,label='Category')
    s_gender = forms.CharField(max_length=30,label='Gender')

class SForm(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student name')