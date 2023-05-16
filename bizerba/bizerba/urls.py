from django.contrib import admin
from django.urls import path

from mainapp.views import JobAPIView, JobAPIUpdate, JobAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/job/', JobAPIView.as_view()),
    path('api/v1/job/<int:pk>', JobAPIUpdate.as_view()),
    path('api/v1/jobdetail/<int:pk>', JobAPIDetailView.as_view())
]
