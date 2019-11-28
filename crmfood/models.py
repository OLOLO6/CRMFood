from django.db import models


class Table(models.Model):
    name = models.CharField('Table`s name', max_length=50, default='')

class Role(models.Model):
    name = models.CharField('Role`s name', max_length=50, default='')

class Status(models.Model):
    name = models.CharField('Your action', max_length=30, default='')

class Department(models.Model):
    name = models.CharField('Department`s name', max_length=50, default='')

class ServicePercentage(models.Model):
    percentage = models.PositiveIntegerField('Service')

class User(models.Model):
    name = models.CharField('Your name', max_length=20, default='')
    surname = models.CharField('Your surname', max_length=20, default='')
    email = models.CharField('Your email', max_length=20, default='')
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, default='', verbose_name='Your role here')
    dateofadd = models.DateField (verbose_name='Date of registration')
    phone = models.CharField('Your phone', max_length=20, default='')

class MealCategory(models.Model):
    name = models.CharField('Category', max_length=30, default='')
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE, default='', verbose_name='Department')

class Meal(models.Model):
    name = models.CharField('Meal`s name', max_length=50, default='')
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE, default='', verbose_name='Category')
    price = models.PositiveIntegerField('Price of meal')
    description = models.CharField('Optimal description', max_length=50, default='')

class Mealsid(models.Model):
    name = models.ForeignKey(Meal, on_delete=models.CASCADE, default='', verbose_name='Meal`s name')
    count = models.IntegerField(verbose_name='Count of meals')

class Order(models.Model):
    waiterid = models.ForeignKey(Role, on_delete=models.CASCADE, default='', verbose_name='Waiter')
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE, default='')
    isitopen = models.CharField('Time', max_length=50, default='',)
    date = models.DateTimeField(verbose_name='Time of order')
    mealsid = models.ManyToManyField(Mealsid, verbose_name='Name of meal')


class Check(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, default='', verbose_name='Order')
    date = models.DateField('Date of check', max_length=20, default='')
    servicefee = models.PositiveIntegerField('Service fee')
    totalsum = models.PositiveIntegerField('Total sum in check')
    meals = models.ManyToManyField(Meal, verbose_name='Name of meal')


class MealsToOrder(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, default='', verbose_name='Order')
    meals = models.ManyToManyField(Mealsid, verbose_name='Name of meal')
