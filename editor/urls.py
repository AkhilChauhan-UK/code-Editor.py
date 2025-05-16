from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # serve editor at root
    path('run/', views.run_code, name='run_code'), # run code API
]
    