from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, "positions.html", context={"resumes": resumes})


class ResumeCreateView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_staff and request.user.is_authenticated:
            Resume.objects.create(
                author_id = request.user.id,
                description = request.POST.get("description")
            )
            return redirect("/home")
        else:
            return HttpResponse(status=403)
