from django.urls import path
from crmfood import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns=[
path('table',views.TableView.as_view()),
path('role',views.RoleView.as_view()),
path('department',views.DepartmentView.as_view()),
path('user',views.UserView.as_view()),
path('mealCategory',views.MealCategoryView.as_view()),
path('status',views.StatusView.as_view()),
path('service',views.ServicePercentageView.as_view()),
path('meal',views.MealView.as_view()),
path('order',views.OrderView.as_view()),
path('check',views.CheckView.as_view()),
path('mealsto',views.MealsToOrderView.as_view()),
path('table/<int:pk>',views.TableDetail.as_view()),
path('role/<int:pk>',views.RoleDetail.as_view()),
path('department/<int:pk>',views.DepartmentDetail.as_view()),
path('user/<int:pk>',views.UserDetail.as_view()),
path('mealcategory/<int:pk>',views.MealCategoryDetail.as_view()),
path('status/<int:pk>',views.StatusDetail.as_view()),
path('meal/<int:pk>',views.MealDetail.as_view()),
path('order/<int:pk>',views.OrderDetail.as_view()),
path('check/<int:pk>',views.CheckDetail.as_view()),
path('mealto/<int:pk>',views.MealsToOrderDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns=format_suffix_patterns(urlpatterns)
