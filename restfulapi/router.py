from employeeapi.viewsets import EmployeeViewset, ControllerViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('iotdevices', ControllerViewset)


# localhost:p/api/
# GET, POST, UPDATE, DELETE
# list, retrive