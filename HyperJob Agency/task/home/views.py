from django.shortcuts import render
from django.views import View
from django import forms
from resume.models import Resume
from vacancy.models import Vacancy


class ProfileForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        vacancies = Vacancy.objects.all()
        return render(request, "profile.html", context={"resumes": resumes, "vacancies": vacancies, "form": ProfileForm()})
