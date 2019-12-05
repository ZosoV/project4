from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import School, Review, Project 
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def index(request):
    # Verification if the user is not register 
    if not request.user.is_authenticated:
        return redirect('login')
    
    schools = School.objects.raw('SELECT * FROM projects_school')

    context = {
        'schools' : schools,
        'username' : request.user.username 
        }

    return render(request, "projects/index.html",context)

def school(request,school_code):
    try:
        school = School.objects.get(code=school_code)

    except School.DoesNotExist:
        raise render(request, "projects/error.html",{"message": "No School."})

    context = {
        "school": school,
        "projects": school.projects_school.all()
    }

    return render(request, "projects/school.html", context)

def project(request, school_code, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise render(request, "projects/error.html",{"message": "No Project."})

    can_comment = False
    try:       
        current_user_review = Review.objects.get(project = project, user = request.user)
    except Review.DoesNotExist:
        can_comment = True

    own_user = project.user == request.user

    context = {
        "project": project,
        "reviews": Review.objects.filter(project = project),
        "can_comment" : can_comment,
        "own_user" : own_user
    }

    return render(request, "projects/project.html", context)

def create_project(request):    
    return render(request, "projects/create_project.html")

def submit_project(request):
    try:
        name = str(request.POST["name"])
        description = str(request.POST["description"])
        state = str(request.POST["state"])
        school_code = str(request.POST["school_code"])
        school = School.objects.get(code=school_code)
    except KeyError:
        return render(request, "projects/error.html",{"message": "No selection."})
    except School.DoesNotExist:
        return render(request, "projects/error.html",{"message": "No School."})

    project = Project(name=name,description=description,state=state,school=school,user=request.user)
    project.save()

    return HttpResponseRedirect(reverse("project",args=(school.code, project.id,)))

def submit_comment(request, school_code, project_id):
    try:
        user = request.user
        comment = str(request.POST["comment"])
        project = Project.objects.get(id = project_id)
    except KeyError:
        return render(request, "projects/error.html",{"message": "No selection."})
    except Project.DoesNotExist:
        return render(request, "projects/error.html",{"message": "No Project." })
    except User.DoesNotExist:
        return render(request, "projects/error.html",{"message": "No User."})    
    
    review = Review(user = user, project = project, comment = comment)
    review.save()

    return HttpResponseRedirect(reverse("project",args=(school_code, project_id,)))

def list_projects(request, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return render(request, "projects/error.html", {"message" : "No User."})
    
    # projects = Project.objects.filter(user = user)
    projects = Project.objects.raw('SELECT * FROM projects_project WHERE user_id = %s',[user.id])

    context = {
        "projects": projects,
        "username": username
    }

    return render(request, "projects/list_project.html", context)
