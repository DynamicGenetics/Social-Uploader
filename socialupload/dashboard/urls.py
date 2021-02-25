from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", view=views.dashboard, name="index"),
    path("thanks/", view=views.thanks, name="thanks"),
    path("data-drop/", views.datadrop, name="datadrop"),
]
