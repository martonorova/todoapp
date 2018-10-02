from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r'notes', views.NotesViewSet, base_name = 'notes'
)

urlpatterns = router.urls
