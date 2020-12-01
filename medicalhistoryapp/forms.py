from django import forms
from django.db.models.enums import Choices
from django.forms import ModelForm
from .models import MedicalFormModel

class MedicalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'
        self.fields['allergy'].widget.attrs['class'] = 'form-control'
        self.fields['tobaccoFlag'].widget.attrs['class'] = 'form-control'
        self.fields['alcoholFlag'].widget.attrs['class'] = 'form-control'
        self.fields['medicationFlag'].widget.attrs['class'] = 'form-control'

    COMMONDISEASES = [
        ("1", "None"),
        ("2", "Asthama"),
        ("3", "Cancer"),
        ("4", "Cardiac Disease"),
        ("5", "Diabetes"),
        ("6", "Blood Pressure"),
        ("7", "Psychiatric Disorder")
    ]

    COMMONSYMPTOMS = [
        ("1", "None"),
        ("2", "Cough"),
        ("3", "Cold"),
        ("4", "Fever"),
        ("5", "Chest Pain"),
        ("6", "Weight Gain"),
        ("7", "Weight Loss"),
        ("8", "Bodyache"),
        ("9", "Headache")
    ]

    GENDER = {
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Other")
    }

    diseases = forms.MultipleChoiceField(choices=COMMONDISEASES, widget=forms.CheckboxSelectMultiple)
    symptoms = forms.MultipleChoiceField(choices=COMMONSYMPTOMS, widget=forms.CheckboxSelectMultiple)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = MedicalFormModel
        fields = ['phoneNumber', 'gender', 'diseases', 'symptoms', 'allergy', 'medicationFlag', 'tobaccoFlag', 'alcoholFlag']

