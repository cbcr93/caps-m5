from django.urls import path

from . import views

urlpatterns = [path("accounts/<id_user>/reviews/", views.ReviewView.as_view())]
