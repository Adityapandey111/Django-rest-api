from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register('employees', views.EmployeeViewSet)
urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>',views.EmployeesDetails.as_view()),
    path('', include(routers.urls))
]
