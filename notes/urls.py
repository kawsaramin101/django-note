from django.urls import path

from .views import index, note_details

app_name = "notes"

urlpatterns = [
    path("", index , name="index"),
    path("<str:secondary_id>/", note_details, name="note_details"),

]
