from django.db import models

# Create your models here.
# Create your models here.
class IMG(models.Model):
    img=models.ImageField(upload_to='upload')

class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, verbose_name=u"主键", max_length=20, default="")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name
        # 指定数据库的表名
        # db_table = "user_message"
        # 排序
        # ordering = "-object_id"
class MyTask(models.Model):
    planid=models.CharField(primary_key=True, verbose_name=u"主键", max_length=20, default="")
    task_name=models.CharField(max_length=100, verbose_name=u"任务名称")
    urladdres=models.CharField(max_length=500, verbose_name=u"任务地址")
    oprate=models.CharField(max_length=200,verbose_name=u"执行")

    def __str__(self):
        return self.name