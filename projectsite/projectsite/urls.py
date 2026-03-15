"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from taskmanager.views import HomePageView, TaskList, TaskCreateView, TaskUpdateView, TaskDeleteView
from taskmanager.views import PriorityList, PriorityUpdateView, PriorityDeleteView
from taskmanager.views import CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from taskmanager.views import SubTaskList, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView
from taskmanager.views import NoteList, NoteCreateView, NoteUpdateView, NoteDeleteView
from taskmanager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', HomePageView.as_view(), name='home'),
    path('task_list', TaskList.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),

    path('priority_list', views.PriorityList.as_view(), name='priority-list'),
    path('priority_list/add', views.PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', views.PriorityDeleteView.as_view(), name='priority-delete'),

    path('category_list', views.CategoryList.as_view(), name='category-list'),
    path('category_list/add', views.CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('subtask_list', views.SubTaskList.as_view(), name='subtask-list'),
    path('subtask_list/add', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('note_list', views.NoteList.as_view(), name='note-list'),
    path('note_list/add', views.NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>', views.NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
]
