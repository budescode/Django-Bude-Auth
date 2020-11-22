from django.urls import path
from .views import SocialUserAuth, RegisterUserView, LoginUserView, UserDetails, ChangePasswordView
urlpatterns = [
    path('authenticatesocialuser', SocialUserAuth.as_view(), name='authenticatesocialuser'),
    path('token/createuser', RegisterUserView.as_view(), name='createuser'),
    path('token/login', LoginUserView.as_view(), name='login'),
    path('token/getuser', UserDetails.as_view(), name='getuser'),
    path('token/changepassword', ChangePasswordView.as_view(), name='changepassword'),
    #path('createuser', UserCreateView.as_view(), name='createuser'),
]
