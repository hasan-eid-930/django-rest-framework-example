from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('ratings', views.RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test',views.test)
]