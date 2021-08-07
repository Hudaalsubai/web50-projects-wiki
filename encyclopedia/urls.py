from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random_entry",views.random_entry,name="random_entry"),
    path("edit_entry/<str:entryTitle>",views.edit_entry,name="edit_entry"),
    path("create_entry",views.create_entry,name="create_entry")

]
