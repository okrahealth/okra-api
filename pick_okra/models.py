from django.db import models

class Repository(models.Model):
    repo_id = models.CharField(max_length=200)

class RepositoryMetrics(models.Model):
    repo_id = models.CharField(max_length=200)
    rating = models.FloatField()

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ForeignKey('Repository', on_delete=models.CASCADE)

class RepositoryInfo(models.Model):
    repo_id = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    namespace = models.CharField(max_length=50)
    firstCommitDate = models.DateTimeField()
    contibutors = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    metrics = models.ForeignKey('RepositoryMetrics', on_delete=models.CASCADE)
