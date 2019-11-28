from rest_framework import serializers
from crmfood.models import *
from django.contrib.auth.models import User


class Table_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'name')

class Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class Status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')

class Department_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class ServicePercentage_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('id', 'percentage')

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email', 'roleid', 'dateofadd', 'phone')

class MealCategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ('id', 'name', 'departmentid')

class Meal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'categoryid', 'price', 'description')

class Mealsid_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mealsid
        fields = ('id', 'name', 'count')

class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'waiterid', 'tableid', 'isitopen', 'date', 'mealsid')

class Check_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ('id', 'orderid', 'date', 'servicefee', 'totalsum', 'meals')


class MealsToOrder_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MealsToOrder
        fields = ('id', 'orderid', 'meals')

