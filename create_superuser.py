import os
from django.contrib.auth import get_user_model

User = get_user_model()

# Superuser credentials
username = "admin"
email = "kamleshlovewanshi2000@gmail.com"
password = "Kamlesh@2025"

# Check if superuser exists
user = User.objects.filter(username=username).first()

if user:
    user.set_password(password)  # Update password if user exists
    user.email = email
    user.save()
    print(f"Password updated for existing superuser: {username}")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"New superuser created: {username}")
