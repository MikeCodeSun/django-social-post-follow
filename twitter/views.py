from django.shortcuts import render,redirect
from .models import Profile,Twitter
from .form import TwitterForm

# Create your views here.
def dashboard(request):
  form = TwitterForm(request.POST or None)
  if request.method == 'POST': 
    if form.is_valid():
      twitter = form.save(commit=False)
      twitter.user = request.user
      twitter.save()
      return redirect("twitter:dashboard")
  # form = TwitterForm()  
  twitters = Twitter.objects.filter(
    user__profile__in = request.user.profile.folllows.all()
  ).order_by("-created_at")
  return render(request, 'twitter/dashboard.html', {"form": form, "twitters": twitters})

def profile_list(r):
  profiles = Profile.objects.exclude(user = r.user)

  return render(r, 'twitter/profile_list.html', {"profiles": profiles})

def profile(r, id):
  profile = Profile.objects.get(pk = id)
  # print(profile)
  # follows = profile.folllows.all()
  # print(follows)
  # follower = profile.follow_by.all()
  # print(follower)

  if not hasattr(r.user, 'profile'):
    miss_profile = Profile(user=r.user)
    miss_profile.save()

  if r.method == "POST":
    user_profile = r.user.profile
    data = r.POST
    action = data.get("follow")
    if action == 'follow':
      user_profile.folllows.add(profile)
    else:
      user_profile.folllows.remove(profile)
    user_profile.save()
  return render(r, 'twitter/profile.html', {'profile': profile})
  