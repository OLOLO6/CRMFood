# Generated by Django 2.2.7 on 2019-11-28 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Department`s name')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Meal`s name')),
                ('price', models.PositiveIntegerField(verbose_name='Price of meal')),
                ('description', models.CharField(default='', max_length=50, verbose_name='Optimal description')),
            ],
        ),
        migrations.CreateModel(
            name='Mealsid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Count of meals')),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Meal', verbose_name='Meal`s name')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Role`s name')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField(verbose_name='Service')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='Your action')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Table`s name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='Your name')),
                ('surname', models.CharField(default='', max_length=20, verbose_name='Your surname')),
                ('email', models.CharField(default='', max_length=20, verbose_name='Your email')),
                ('dateofadd', models.DateField(verbose_name='Date of registration')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Your phone')),
                ('roleid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Role', verbose_name='Your role here')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isitopen', models.CharField(default='', max_length=50, verbose_name='Time')),
                ('date', models.DateTimeField(verbose_name='Time of order')),
                ('mealsid', models.ManyToManyField(to='crmfood.Mealsid', verbose_name='Name of meal')),
                ('tableid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Table')),
                ('waiterid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Role', verbose_name='Waiter')),
            ],
        ),
        migrations.CreateModel(
            name='MealsToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meals', models.ManyToManyField(to='crmfood.Mealsid', verbose_name='Name of meal')),
                ('orderid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='Category')),
                ('departmentid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Department', verbose_name='Department')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='categoryid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.MealCategory', verbose_name='Category'),
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='', max_length=20, verbose_name='Date of check')),
                ('servicefee', models.PositiveIntegerField(verbose_name='Service fee')),
                ('totalsum', models.PositiveIntegerField(verbose_name='Total sum in check')),
                ('meals', models.ManyToManyField(to='crmfood.Meal', verbose_name='Name of meal')),
                ('orderid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crmfood.Order', verbose_name='Order')),
            ],
        ),
    ]