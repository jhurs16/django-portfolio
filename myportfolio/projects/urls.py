from django.urls import path
from projects.views import ListProjects

urlpatterns = [
    path('', ListProjects.as_view(), name="projects"),
]