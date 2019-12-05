from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_projects/<str:username>", views.list_projects, name="list_projects"),
    path("create_project", views.create_project , name="create_project"),
    path("new_project", views.submit_project, name="submit_project"),
    path("home/<str:school_code>/<int:project_id>/submit_comment", views.submit_comment, name="submit_comment"),
    path("home/<str:school_code>/<int:project_id>", views.project, name="project"),
    path("home/<str:school_code>", views.school, name="school"),
]