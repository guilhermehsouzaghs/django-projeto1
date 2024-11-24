from django.urls import path
from recipes.views import home,recipe

urlpatterns = [
    path('',home),
    path('recipes/<int:id>/',recipe),
]