"""Defines URL pattenrs for job_apps"""

from django.urls import path

from . import views

app_name = 'job_apps'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Application Entry Log
    path('job_log/', views.job_log, name='job_log'),
    # Details page for job entry
    path('job_log/<int:job_entry_id>/', views.job_entry, name='job_entry'),
    # Page for adding new entry
    path('new_job_entry/', views.new_job_entry, name='new_job_entry'),
    # Page for editing an entry
    path('edit_job_entry/<int:job_entry_id>/',
         views.edit_job_entry, name='edit_job_entry'),
]
