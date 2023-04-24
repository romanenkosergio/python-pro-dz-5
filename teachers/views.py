from django.shortcuts import render

from .models import Teacher


def home(request):
    """Home page."""
    return render(request, "home.html", {"title": "Home"})


def get_teachers_list(request):
    """Get all teachers."""
    teachers = Teacher.objects.all().values()
    return render(
        request, "all_teachers.html", {"teachers": teachers, "title": "All Teachers"}
    )
