# Generated by Django 2.2.5 on 2019-09-26 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_categorie_nom_auteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('nom_auteur', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('statut', models.BooleanField(default=0)),
                ('image', models.ImageField(upload_to='img')),
                ('article', models.TextField()),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_detail', to='blogapp.Categorie')),
            ],
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
