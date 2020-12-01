from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .forms import MedicalForm
from .models import MedicalFormModel
from django.contrib.auth.models import User

@login_required(login_url='user/login/')
def homePage(request):
    UserInfo = apps.get_model('userauthentication', 'AdditionalUserInformation')
    user = UserInfo.objects.get(username=request.user)
    form = MedicalForm()
    if user.userType == 1:
        context = {
            "username": user.username,
            "userId": user.userId,
            "medicalForm": form
        }
        if request.method == 'POST':
            saveMedicalForm(request.POST, user.userId)
        return render(request, 'medicalhistoryapp/patient.html', context=context)
    else:
        context = {
            "username": user.username,
            "userId": user.userId,
        }
        if 'search' in request.GET:
            diseases = {
                '1': 'None',
                '2': 'Asthama',
                '3': 'Cancer',
                '4': 'Cardiac Disease',
                '5': 'Diabetes',
                '6': 'Blood Pressure',
                '7': 'Psychiatric Disorder',
            }
            symptoms = {
                '1': 'None',
                '2': 'Cough',
                '3': 'Cold',
                '4': 'Fever',
                '5': 'Chest Pain',
                '6': 'Weight Gain',
                '7': 'Weight Loss',
                '8': 'Bodyache',
                '9': 'Headache',
            }
            diseasesList = []
            symptomsList = []
            enteredUserId = request.GET['search']
            queryResult = MedicalFormModel.objects.get(userId = enteredUserId)
            intermediateQuery = UserInfo.objects.get(userId = enteredUserId)
            userResult = User.objects.get(username = intermediateQuery.username)
            if queryResult is not None:
                context["entryFlag"] = True
                context["firstname"] = userResult.first_name
                context["lastname"] = userResult.last_name
                context["gender"] = queryResult.gender
                context["alcohol"] = queryResult.alcoholFlag
                context["tobacco"] = queryResult.tobaccoFlag
                context["medication"] = queryResult.medicationFlag
                for item in queryResult.commonDiseases.split(","):
                    diseasesList.append(diseases[item])
                context["diseases"] = diseasesList
                for item in queryResult.commonSymptoms.split(","):
                    symptomsList.append(symptoms[item])
                context["symptoms"] = symptomsList
                context["phonenumber"] = queryResult.phoneNumber
                context["allergy"] = queryResult.allergy
            else:
                context["entryFlag"] = False
                context["message"] = "No History Found"
        return render(request, 'medicalhistoryapp/doctor.html', context=context)


def saveMedicalForm(rawData, userId):
    genderDict = {
        "1": "Male",
        "2": "Female",
        "3": "Other"
    }
    form = MedicalForm(rawData)
    if form.is_valid():
        formInfo = MedicalFormModel()
        formInfo.phoneNumber = form.data['phoneNumber']
        formInfo.medicationFlag = form.data['medicationFlag']
        formInfo.alcoholFlag = form.data['alcoholFlag']
        formInfo.tobaccoFlag = form.data['tobaccoFlag']
        formInfo.commonDiseases = getListData(rawData.getlist('diseases'))
        formInfo.commonSymptoms = getListData(rawData.getlist('symptoms'))
        formInfo.gender = genderDict[form.data['gender']]
        formInfo.userId = userId
        formInfo.allergy = form.data['allergy']
        formInfo.save()


def getListData(list):
    savestr = ""
    for item in list:
        savestr += str(item) + ","
    return savestr[0:len(savestr)-1]