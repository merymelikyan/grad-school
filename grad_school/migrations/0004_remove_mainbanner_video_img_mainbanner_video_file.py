# Generated by Django 5.2 on 2025-05-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grad_school', '0003_remove_mainbanner_video_url_mainbanner_video_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainbanner',
            name='video_img',
        ),
        migrations.AddField(
            model_name='mainbanner',
            name='video_file',
            field=models.FileField(blank=True, db_index=True, null=True, upload_to='videos/'),
        ),
    ]
