from rest_framework import serializers

from pick_okra.models import Contributor
from pick_okra.models import Repository
from pick_okra.models import RepositoryInfo
from pick_okra.models import RepositoryMetrics


class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repository
        fields = ['repo_id']

class RepositoryMetricsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepositoryMetrics
        fields = '__all__'

class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class RepositoryInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepositoryInfo
        fields = '__all__'
