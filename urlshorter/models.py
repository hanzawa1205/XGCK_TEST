from django.db import models

# Create your models here.


class Link(models.Model):
    url = models.TextField("长网址")
    short_link = models.CharField("短链接", max_length=16)

    class Meta:
        db_table = "link_map"
        verbose_name = "网址映射"
        verbose_name_plural = verbose_name


class IpVisitNumber(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数

    class Meta:
        db_table = 'IpVisitNumber'
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name


class VisitNumber(models.Model):
    count = models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数

    class Meta:
        db_table = 'VisitNumber'
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name
