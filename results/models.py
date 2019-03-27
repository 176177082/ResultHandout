# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Result(models.Model):
    path = models.CharField(max_length=5000, null=True, blank=True,verbose_name=u"文件路径")
    pathdeep = models.IntegerField(default=0, null=True, blank=True,verbose_name=u"文件路径深度")
    pathlength = models.IntegerField(default=0, null=True, blank=True,verbose_name=u"文件路径长度")

    class Meta:
        verbose_name = u"成果路径表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.path