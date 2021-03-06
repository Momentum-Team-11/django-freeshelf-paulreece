# Generated by Django 4.0.3 on 2022-03-08 15:59

from __future__ import unicode_literals
import csv
from django.db import migrations, models
from datetime import datetime


def load_initial_data(apps, schema_editor):
    Book = apps.get_model("books", "Book")

    with open("sample_books.csv") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        books = []

        for row in reader:
            # camis = row[0]
            # book = next((b for b in books if b.camis == camis), None)
            book = Book(
                title=row[0],
                author=row[1],
                url=row[2],
                description=row[3],
                date=datetime.now(),
                pic="",
            )
            books.append(book)
        Book.objects.bulk_create(books)


def reverse_func(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Book.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_book"),
    ]

    operations = [migrations.RunPython(load_initial_data, reverse_func)]
