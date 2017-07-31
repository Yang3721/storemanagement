from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
#    list_display = ('user_name','user_email','user_password')
#    list_editable = ('user_email','user_password')
    list_display = ('name','jobNum','department','email','tel','password','remarks')
    list_editable =('jobNum','department','email','tel','password','remarks')


#class Materials_allAdmin(admin.ModelAdmin):
    #list_display = ('name','type', 'modelNum', 'storoomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'usefulLife', 'serialNum', 'countingUnit', 'core_Num', 'measurement', 'mountingNum', 'threshold', 'remarks')
    #, 'modelNum', 'storoomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'usefulLife', 'serialNum', 'countingUnit', 'coreNum', 'measurement', 'mountingNum', 'threshold', 'remarks'
    #list_editable = ('type','modelNum', 'storoomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'usefulLife', 'serialNum', 'countingUnit', 'core_Num', 'measurement', 'mountingNum', 'threshold', 'remarks')
    #'modelNum', 'storoomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'usefulLife', 'serialNum', 'countingUnit', 'coreNum', 'measurement', 'mountingNum', 'threshold', 'remarks'


class all_objectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'modelNum', 'roomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'useLife', 'serialNum', 'countingUnit', 'coreNum', 'measurement', 'mountingNum', 'threshold', 'remarks')
    list_editable = ('type', 'modelNum', 'roomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'useLife', 'serialNum', 'countingUnit', 'coreNum', 'measurement', 'mountingNum', 'threshold', 'remarks')


class ReturnManagementAdmin(admin.ModelAdmin):
    list_display = ('formNum_de','operator_re','deliveryDate','returnDate','type','storageroom','manager','materialName','modelNum','storoomNum','returnState','attachState','returnNum','remarks')
    list_editable = ('operator_re','deliveryDate','returnDate','type','storageroom','manager','materialName','modelNum','storoomNum','returnState','attachState','returnNum','remarks')


admin.site.register(Staff,StaffAdmin)


admin.site.register(all_object,all_objectAdmin)


admin.site.register(ReturnManagement,ReturnManagementAdmin)