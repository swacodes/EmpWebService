"""EmpWebService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from empapp.views import get_employee_max_direct_subordinates, change_manager, get_total_salary_subordinate, \
    print_org_structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeServices/max-subordinates/', get_employee_max_direct_subordinates,
         name='get_employee_max_direct_subordinates'),
    path('employeeServices/change-manager/<int:emp_id>/<int:mgr_id>/', change_manager, name='change_manager'),
    path('employeeServices/total-subordinate-salary/<int:mgr_id>/', get_total_salary_subordinate,
         name='get_total_salary_subordinate'),
    path('employeeServices/organisation-structure/', print_org_structure, name='print_org_structure'),

]
