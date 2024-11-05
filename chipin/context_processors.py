from users.models import Profile
def user_profile(request):
    if request.user.is_authenticated:
        try:
            return {'nickname': request.user.profile.nickname}
        except Profile.DoesNotExist:
            return {'nickname': request.user.username}  # Fallback to username if no profile exists
    return {}