from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='url_home'),
    path('description/<int:id>/', item_description, name='url_item_description'),
    path('new_item/', new_item, name='url_new_item'),
    path('new_item_tag/', new_item_tag, name='url_new_item_tag'),
    path('delete_item/<int:id>', delete_item, name="url_delete_item"),
]