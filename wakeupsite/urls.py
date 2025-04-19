from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("wakeapp/", include("wakeapp.urls")),
    path("admin/", admin.site.urls),
]