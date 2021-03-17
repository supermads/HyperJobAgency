from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vacancy



class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, "openings.html", context={"vacancies": vacancies})


class VacancyCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_authenticated:
            Vacancy.objects.create(
                description=request.POST.get("description"),
                author_id=request.user.id
            )
            return redirect("/home")
        else:
            return HttpResponse(status=403)
