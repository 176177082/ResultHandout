# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from results.models import Result
from results.serializers import ResultsSerializer

class ResultsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Result.objects.all()
    serializer_class = ResultsSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]