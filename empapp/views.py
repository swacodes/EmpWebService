from django.shortcuts import render
from empapp.models import Employee
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import networkx as nx
import matplotlib.pyplot as py
from treelib import node, Tree


def get_employee_max_direct_subordinates(request):
    try:
        employees = Employee.objects.all()
        inter_result = employees.values('manager_emp_id').annotate(total=Count('manager_emp_id')).order_by('-total')
    except ObjectDoesNotExist:
        return JsonResponse({'Exception': 'Maximum direct subordinates is not found'})
    result = inter_result.first()
    return JsonResponse(result, safe=False)


def change_manager(request, emp_id, mgr_id):
    try:
        employee = Employee.objects.get(employee_id=emp_id)
    except ObjectDoesNotExist:
        return JsonResponse({'Exception': 'Employee is not in the records'})
    try:
        Employee.objects.get(employee_id=mgr_id)
    except ObjectDoesNotExist:
        return JsonResponse({'Exception': 'Manager is not in the records'})
    employee.manager_emp_id = mgr_id
    employee.save()
    return JsonResponse({'message': 'Manager changed successfully'}, safe=False)


def get_total_salary_subordinate(request, mgr_id):
    try:
        Employee.objects.all().get(employee_id=mgr_id)
    except ObjectDoesNotExist:
        return JsonResponse({'Exception': 'Manager is not in the records'})
    try:
        Employee.objects.all().filter(manager_emp_id=mgr_id).first()
    except ObjectDoesNotExist:
        return JsonResponse({'Exception': 'Employee is not a manager'})
    result = Employee.objects.all().filter(manager_emp_id=mgr_id).aggregate(total_salary=Sum('salary'))
    return JsonResponse(result, safe=False)


def print_org_structure(request):
    org_map = {}
    for emp in Employee.objects.all():
        if emp.manager_emp_id not in org_map:
            org_map[emp.manager_emp_id] = [emp.employee_id]
        else:
            current = org_map[emp.manager_emp_id]
            current.append(emp.employee_id)
            org_map[emp.manager_emp_id] = current
    print(org_map)

    return JsonResponse(org_map, safe=False)
