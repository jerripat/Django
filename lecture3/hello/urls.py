
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("jerri", views.jerri, name="jerri"),
    path("<str:name>", views.greet, name="greet")

]