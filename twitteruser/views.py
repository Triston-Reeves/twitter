from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import Twitter_user
from twitteruser.forms import AddSignupForm
from tweet.models import Tweet

@login_required
def index_view(request):
    my_tweets = Tweet.objects.all()
    return render(request, "index.html", {"my_tweets": my_tweets})

def signup_view(request):
    if request.method == "POST":
        form = AddSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Twitter_user.objects.create_user(
                username=data.get("username"), 
                password=data.get("password")
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))

    form = AddSignupForm()
    return render(request, "generic_form.html", {"form": form})



# def following_view(request, follow_id):
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# def unfollowing_view(request, unfollow_id):
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


