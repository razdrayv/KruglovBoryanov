# Generated by Django 3.2 on 2023-09-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Название', 'verbose_name_plural': 'Названия'},
        ),
        migrations.AlterField(
            model_name='category',
            name='nameCategory',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='img/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='made',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
