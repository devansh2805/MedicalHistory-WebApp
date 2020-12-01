from django.db import models
from django.core.validators import RegexValidator, validate_comma_separated_integer_list

class MedicalFormModel(models.Model):
    phoneRegex = RegexValidator(regex=r'^\d{10}', message="Phone Number must be of 10 digits")
    booleanChoices = ((True, "Yes"), (False, "No"))
    commonDiseases = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    commonSymptoms = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    allergy = models.CharField(max_length=100)
    tobaccoFlag = models.BooleanField(choices=booleanChoices, default=False)
    alcoholFlag = models.BooleanField(choices=booleanChoices, default=False)
    medicationFlag = models.BooleanField(choices=booleanChoices, default=False)
    gender = models.CharField(max_length=6)
    phoneNumber = models.CharField(validators=[phoneRegex], max_length=10)
    userId = models.CharField(max_length=6)