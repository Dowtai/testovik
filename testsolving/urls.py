from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('create-test/', views.create_test, name='create_test'),
    path('add-questions/<int:test_id>/', views.add_questions, name='add_questions'),
    path('solve-test/<int:test_id>/', views.solve_test, name='solve_test'),
    path('test-results/<int:test_id>/', views.test_results, name='test_results'),
    path('tests/<int:test_id>/delete/', views.test_delete, name='test_delete'),
    path('result/<int:result_id>/', views.result, name='result')
]