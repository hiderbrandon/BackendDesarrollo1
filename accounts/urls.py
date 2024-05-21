#Profile


from django.urls import path
from .views import MyTokenObtainPairView , RegisterView ,deleteProfile ,updateProfile ,getProfile,list_users
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    #path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<int:userId>/', getProfile, name='getProfile'),
    path('profile/update/', updateProfile, name='update_profile'),  
    path('profile/delete/', deleteProfile, name='delete_profile'),  # URL para eliminar el perfil
    path('profile/allusers/',list_users, name='user-list'),

]