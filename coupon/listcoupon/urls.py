from django.urls import path
from . import views
urlpatterns = [
    path('ma-giam-gia/', views.index_mgg, name = "index_mgg" ),
    path('khuyen-mai/', views.category, name = "category" ),
]