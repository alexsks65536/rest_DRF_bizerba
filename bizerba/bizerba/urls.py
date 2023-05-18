from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

# from mainapp.views import JobAPIView, JobAPIUpdate, JobAPIDetailView, SparePartAPIDetailView, SparePartAPIView
from mainapp.views import JobViewSet, SparePartViewSet, CustomerViewSet, DepartmentViewSet, ScaleModelViewSet, \
    ScaleViewSet, ReceivingViewSet, InstallationViewSet

router = routers.DefaultRouter()  # инициализация роутера
router.register(r'job', JobViewSet)  # заявки в работу
router.register(r'spare', SparePartViewSet)  # запчасти с артикулами
router.register(r'customer', CustomerViewSet)  # заказчики
router.register(r'department', DepartmentViewSet)  # Отделы
router.register(r'scalemodel', ScaleModelViewSet)  # Модели весов
router.register(r'scale', ScaleViewSet)  # Список весов
router.register(r'receiving', ReceivingViewSet)  # Приход ЗИП
router.register(r'installation', InstallationViewSet)  # Установка ЗИП


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/job/', JobAPIView.as_view()),  # заявки в работу
    # path('api/v1/job/<int:pk>', JobAPIUpdate.as_view()),  # заявки в работу
    # path('api/v1/jobdetail/<int:pk>', JobAPIDetailView.as_view()),  # заявки в работу
    # path('api/v1/sparepart/', SparePartAPIView.as_view()),  # запчасти с артикулами
    # path('api/v1/sparedetail/<int:pk>', SparePartAPIDetailView.as_view()),  # запчасти с артикулами
]
