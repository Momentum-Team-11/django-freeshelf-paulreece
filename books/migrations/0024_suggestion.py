# Generated by Django 4.0.3 on 2022-03-09 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.CharField(max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pic', models.ImageField(blank=True, upload_to='')),
                ('favorite', models.CharField(blank=True, max_length=200, null=True)),
                ('favorited_number', models.IntegerField(default=0)),
                ('favorite_date', models.DateTimeField(blank=True, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(blank=True, to='books.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
