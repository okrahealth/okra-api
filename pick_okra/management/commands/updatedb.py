import logging

from django.core.management.base import BaseCommand, CommandError
from pick_okra.models import (Repository, RepositoryMetrics,
                              Contributor, RepositoryInfo)

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'updates db with new records'

    def add_arguments(self, parser):
        parser.add_argument('pq_files', nargs='+', type=str)

    def handle(self, *args, **options):
        for pq_file in options['pq_files']:
            print('pq_file: {}'.format(pq_file))
            
