# Generated by Django 5.2 on 2025-05-14 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Blog Names',
                'verbose_name_plural': 'Blog Names',
            },
        ),
        migrations.CreateModel(
            name='Choosetab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Choosetab',
                'verbose_name_plural': 'Choosetab',
            },
        ),
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('title3', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Coming Soon',
                'verbose_name_plural': 'Coming Soon',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description1', models.CharField(blank=True, max_length=500, null=True)),
                ('description2', models.CharField(blank=True, max_length=500, null=True)),
                ('icon_class', models.CharField(blank=True, help_text='FontAwesome icon', max_length=50, null=True)),
                ('link_name', models.CharField(blank=True, max_length=55, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Features',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=255, null=True)),
                ('text2', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=55, null=True)),
                ('title2', models.CharField(blank=True, max_length=55, null=True)),
                ('icon_class', models.CharField(blank=True, help_text='FontAwesome icon', max_length=50, null=True)),
                ('link_url1', models.URLField(blank=True, null=True)),
                ('link_url2', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text1', models.CharField(blank=True, max_length=55, null=True)),
                ('text2', models.CharField(blank=True, max_length=55, null=True)),
                ('video_url', models.URLField(db_index=True)),
                ('link_name', models.TextField(max_length=55)),
                ('link_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Main Banner',
                'verbose_name_plural': 'Main Banner',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('title3', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phon_number', models.CharField(max_length=100)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Registration',
                'verbose_name_plural': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='Section_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, max_length=50, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='courses')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='author')),
                ('icon_class', models.CharField(blank=True, help_text='FontAwesome icon', max_length=50, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Section_courses',
                'verbose_name_plural': 'Section_courses',
            },
        ),
        migrations.CreateModel(
            name='Section_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('description1', models.TextField(blank=True, max_length=500, null=True)),
                ('description2', models.TextField(blank=True, max_length=500, null=True)),
                ('description3', models.TextField(blank=True, max_length=500, null=True)),
                ('link_name1', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url1', models.URLField(blank=True, null=True)),
                ('link_name2', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url2', models.URLField(blank=True, null=True)),
                ('video_name', models.TextField(blank=True, max_length=50, null=True)),
                ('video_url', models.URLField(db_index=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='main')),
            ],
            options={
                'verbose_name': 'Section_video',
                'verbose_name_plural': 'Section_video',
            },
        ),
        migrations.CreateModel(
            name='SectionsMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('link_name', models.TextField(blank=True, max_length=55, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Sections Menu',
                'verbose_name_plural': 'Sections Menu',
            },
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tabs_id', models.CharField(max_length=100, unique=True)),
                ('description1', models.CharField(blank=True, max_length=500, null=True)),
                ('description2', models.CharField(blank=True, max_length=500, null=True)),
                ('description3', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='choose')),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tabs',
                'verbose_name_plural': 'Tabs',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Վերնագիր')),
                ('value', models.CharField(max_length=10, verbose_name='Արժեք')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Հերթականություն')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Time',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('href', models.CharField(max_length=200)),
                ('is_external', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_items', to='grad_school.menuitem')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
                'ordering': ['order'],
            },
        ),
    ]
