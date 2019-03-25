# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Result(models.Model):
	path = models.CharField(max_length=5000)
	def __str__(self):
		return self.question_text