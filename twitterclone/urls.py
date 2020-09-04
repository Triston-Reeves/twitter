"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as User_view
from authentication import views as Auth_views
from notification import views as Note_views
from tweet import views as Tweet_views

urlpatterns = [
    path('', User_view.index_view, name="homepage"),
    path('login/', Auth_views.login_view, name="login_view"),
    path('logout/', Auth_views.logout_view, name="logout_view"),
    # path('follow/<int:follow_id>/', views.following_view), 
    # path('unfollow/<int:unfollow_id>/', views.unfollowing_view),
    path('addtweet/', Tweet_views.add_tweet, name="add_tweet"),
    path('signup/', User_view.signup_view, name="signup_view"),
    path('admin/', admin.site.urls),
]
