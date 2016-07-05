from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import login

import views,todoviews
urlpatterns = [
    url(r'^$',view=todoviews.TodoListView.as_view(),name="display-lists"),
    url(r'^lists/update/(?P<pk>[0-9]+)',view=todoviews.TodoUpdateView.as_view(),name="update-list"),
    url(r'^lists/delete/(?P<pk>[0-9]+)',view=todoviews.TodoDeleteView.as_view(),name="delete-list"),
    url(r'^lists/create',view=todoviews.TodoCreateView.as_view(),name="create-list"),
    url(r'^lists/(?P<id>[0-9]+)',view=todoviews.TodoDetailsView.as_view(),name="display-items"),
    url(r'^items/create',view=todoviews.TodoItemCreateView.as_view(),name="create-item"),
    url(r'^items/update/(?P<pk>[0-9]+)',view=todoviews.TodoItemUpdateView.as_view(),name='update-item'),
    url(r'^items/delete/(?P<pk>[0-9]+)',view=todoviews.TodoItemDeleteView.as_view(),name='delete-item'),
    url(r'^items/(?P<id>[0-9]+)',view=todoviews.TodoItemDetailsView.as_view(),name="display-details")
    # url(r'^lists', views.lists, name="text"),
    # url(r'^todo/(?P<id>[0-9]+)', views.text, name="details-based-on-id"),
    #
    # url(r'^lists/create$',view=todoviews.TodoCreateView.as_view()),

    # url(r'^lists',view=todoviews.TodoListView.as_view(),name="display-lists"),
]