from django.urls import path , include
from .api import TodoViewset
from rest_framework.routers import DefaultRouter
from .views import todo_list

router = DefaultRouter()
router.register('',TodoViewset)


urlpatterns = [
    path('', todo_list),
    path('api/' , include(router.urls)),
]

