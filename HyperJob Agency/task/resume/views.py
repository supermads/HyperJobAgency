from django.views import View
from django.shortcuts import render
from .models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, "positions.html", context={"resumes": resumes})
