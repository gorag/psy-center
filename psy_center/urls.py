from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from clients import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'users', views.UserViewSet)
schema_view = get_schema_view(title='Psy-center API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
