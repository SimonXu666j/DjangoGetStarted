# coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserMessage(models.Model):
    # 设置最大长度，verbose_name在后台显示字段会用到
    name = models.CharField(max_length = 20, verbose_name = u"用户名")
    # Django提供内置的邮箱字段会帮忙验证` default_validators = [validators.validate_email]`
    email = models.EmailField(verbose_name = u"邮箱")
    address = models.CharField(max_length = 100, verbose_name = u"联系地址")
    message = models.CharField(max_length = 500, verbose_name = u"留言信息")
    # object_id必须有默认值
    object_id = models.CharField(max_length = 50, primary_key = True, default = '', verbose_name = u'主键')

    class Meta:
        verbose_name = u"用户留言信息"
        # db_table ，这里我们让它自动生成所以不用指定
        db_table = 'user_message'
        # 复数信息，便于人阅读，否则会在后台显示  用户留言信息s
        verbose_name_plural = verbose_name
        # 这个'ordering' must be a tuple or list ，所以药写成('-object_id',)或者['-object_id']，不能是'-object_id'
        # ordering = ['-object_id']
        ordering = ('-object_id',)