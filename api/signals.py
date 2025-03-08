from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    """Automatically creates a superuser after migrations."""
    if sender.name == "api":  # Ensures this runs only for this app
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "kamleshlovewanshi2000@gmail.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Kamlesh@2025")

        if not User.objects.filter(username=username).exists():
            print("Creating superuser...")
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser created: {username}")
        else:
            print("Superuser already exists.")
