from django.shortcuts import render
from rest_framework import viewsets

from pick_okra.models import Contributor
from pick_okra.models import Repository
from pick_okra.models import RepositoryInfo
from pick_okra.models import RepositoryMetrics

from pick_okra.serializers import ContributorSerializer
from pick_okra.serializers import RepositorySerializer
from pick_okra.serializers import RepositoryInfoSerializer
from pick_okra.serializers import RepositoryMetricsSerializer

class RepositoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that all repo_id: pallet/flask
    """
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    http_method_names = ['get']

class RepositoryMetricsViewSet(viewsets.ModelViewSet):
    """
    Metrics on each repository rating
    """
    queryset = RepositoryMetrics.objects.all()
    serializer_class = RepositoryMetricsSerializer
    http_method_names = ['get']

class ContributorViewSet(viewsets.ModelViewSet):
    """
    Metrics on each contributor
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    http_method_names = ['get']

class RepositoryInfoViewSet(viewsets.ModelViewSet):
    """
    General Metrics on each repository
    """
    queryset = RepositoryInfo.objects.all()
    serializer_class = RepositoryInfoSerializer
    http_method_names = ['get']
    
