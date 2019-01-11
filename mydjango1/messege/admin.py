from django.contrib import admin

# Register your models here.
from messege.models import UserMessage as um
from messege.models import MyTask as mt
#注册
@admin.register(um)#相当于把应用注册了
class UserMessageAdmin(admin.ModelAdmin):

    list_display = ['address','name','email','message']
    list_filter = ['name']#过滤
    search_fields = ['name']#以什么检索
    list_per_page =2

    #添加修改属性
    #fields =
    #fieldsets =
@admin.register(mt)
class MyTaskAdmin(admin.ModelAdmin):
    list_display = ['planid','task_name','urladdres',"oprate"]
    list_filter = ['task_name']
    list_per_page = 10
    list_display_links = ['oprate']
admin.site.site_header = '融贝测试管理系统'
admin.site.site_title = '融贝测试专用'