import pandas as pd
from django.core.management.base import BaseCommand
from reviews.models import Category, Title


class Command(BaseCommand):
    def handle(self, *args, **options):
        tmp_data = pd.read_csv(
            'C:\\Dev\\api_yamdb\\api_yamdb\\static\\data\\titles.csv',
            sep=','
        )
        titles = [
            Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=Category.objects.get(pk=row['category']),
            )
            for i, row in tmp_data.iterrows()
        ]
        Title.objects.bulk_create(titles)
        print('Данные записаны в БД')
