from django.contrib.auth.models import User
from crmfood.serializers import *
from crmfood.models import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import filters
import django_filters
from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView


class TableView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = Table_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = Table_Serializer


class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = Role_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = Role_Serializer


class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = Department_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = Department_Serializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_Serializer


class MealCategoryView(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategory_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MealCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategory_Serializer


class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = Status_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = Status_Serializer


class ServicePercentageView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentage_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ServicePercentageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentage_Serializer


class MealView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = Meal_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = Meal_Serializer


class MealsidView(generics.ListCreateAPIView):
    queryset = Mealsid.objects.all()
    serializer_class = Mealsid_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MealsidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mealsid.objects.all()
    serializer_class = Mealsid_Serializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = Order_Serializer


class CheckView(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = Check_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CheckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Check.objects.all()
    serializer_class = Check_Serializer


class MealsToOrderView(generics.ListCreateAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrder_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MealsToOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrder_Serializer
