from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index, name='my_index'),
    path('process_money', views.process_money, name='my_money'),
    path('reset', views.reset, name='my_reset'),
]