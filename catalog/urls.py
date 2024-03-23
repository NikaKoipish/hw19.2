from django.urls import path
from catalog.views import index_home, index_contacts
urlpatterns = [
    path('catalog/', index_contacts),
    path('', index_home)
]
