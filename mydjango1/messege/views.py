from django.shortcuts import render, redirect
from .models import UserMessage
from messege.models import IMG
from .models import MyTask

# Create your views here.
def showIMG(request):
    img= IMG.objects.all()

def getform(request):
    #获取数据库的所有数据，返回的是可以进行循环的QuerySet类型
    #数据表管理器objects
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message.name)
    #这里的message其实就是UserMessage的实例
    #我们还可以根据条件取出数据
    all_message = UserMessage.objects.filter(name=u"王二小", address=u"杭州")

    return  render(request,'messege.html')
def gettask(request):
    tasklist=MyTask.objects.all()
    return render(request,'task.html')
def geturl(request):
    tasklist = MyTask.objects.all()
   # return render(request,'taskwork.html',)
    obj = MyTask.objects.get('urladdres')
    return redirect(obj)
