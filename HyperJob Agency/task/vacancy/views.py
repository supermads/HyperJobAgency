from django.views import View
from django.shortcuts import render
from .models import Vacancy


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, "openings.html", context={"vacancies": vacancies})
