from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.models import Tweet
from tweet.forms import AddTweetForm

# def tweet_detail(request, tweet_id):
#     my_tweet = Tweet.objects.filter(tweet=tweet_id).first()
#     return render(request, "tweet_detail.html", {"my_tweet": my_tweet})

class TweetDetailView(TemplateView):

    def get(self, request, tweet_id):
        my_tweet = Tweet.objects.filter(tweet=tweet_id).first()
        return render(request, "tweet_detail.html", {"my_tweet": my_tweet})



class AddTweetView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = AddTweetForm()
        return render (request, "generic_form.html", {"form": form})

    def post(self, request):
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                tweet = data.get("tweet"),
                tweet_author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "generic_form.html", {"form": form})

# @login_required
# def add_tweet(request):
#     if request.method == "POST":
#         form = AddTweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Tweet.objects.create(
#                 tweet = data.get("tweet"),
#                 tweet_author = request.user,
#             )
#             return HttpResponseRedirect(reverse("homepage"))
        
#     form = AddTweetForm()
#     return render(request, "generic_form.html", {"form": form})
