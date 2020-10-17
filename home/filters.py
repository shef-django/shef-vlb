import django_filters
from .models import *


class BookFilter(django_filters.FilterSet):
    class Meta:
        model=LibBook
        fields=['book_category','availability','price']
