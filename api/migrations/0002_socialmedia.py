# Generated by Django 5.0.6 on 2024-05-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_link', models.URLField()),
                ('facebook_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('github_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('mail', models.EmailField(max_length=200)),
                ('contact_no', models.CharField(max_length=15)),
            ],
        ),
    ]
