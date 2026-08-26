from rest_framework import viewsets
from Empdetails.models import Employee
from Empdetails.serializer import EmployeeSerializer 

class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer