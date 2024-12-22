# Generated by Django 5.1.4 on 2024-12-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('employment_type', models.CharField(max_length=100)),
                ('posted_date', models.DateTimeField()),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('company_logo_url', models.URLField(blank=True, max_length=500, null=True)),
                ('details_page_url', models.URLField(max_length=500)),
                ('is_remote', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-posted_date'],
            },
        ),
    ]
