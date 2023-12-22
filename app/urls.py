from django.urls import path
from . import views

urlpatterns = [
    # Student
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    # Estimation
    path('estimations/', views.estimation_list, name='estimation_list'),
    path('add_estimation/', views.add_estimation, name='add_estimation'),
    path('edit_estimation/<int:pk>/', views.edit_estimation, name='edit_estimation'),
    path('delete_estimation/<int:pk>/', views.delete_estimation, name='delete_estimation'),

    # Subject
    path('subjects/', views.subject_list, name='subject_list'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_subject/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('delete_subject/<int:pk>/', views.delete_subject, name='delete_subject'),
]