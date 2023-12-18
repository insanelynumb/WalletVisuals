from django.urls import path
from user_preferences import views
app_name = 'user_preferences'
urlpatterns = [
    path('user_preferences/', views.index, name='user_preferences'),

]