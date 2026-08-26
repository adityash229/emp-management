from Empdetails.viewset import Employeeviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Employee', Employeeviewset, basename = 'emplyoee') 