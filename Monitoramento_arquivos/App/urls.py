from django.urls import path
from App.views import home, get_files

urlpatterns = [
    path('', home, name='home'),
    path('get-files/', get_files, name='get_files'),
]
