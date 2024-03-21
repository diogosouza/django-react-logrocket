from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView
)

urlpatterns = [
    path("students/", StudentListView.as_view()),
    path("student/<str:id>/", StudentDetailView.as_view())
]
