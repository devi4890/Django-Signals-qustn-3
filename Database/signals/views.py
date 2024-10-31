from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_user_view(request):
    create_user_with_exception()
    return HttpResponse("User creation tested, check the console.")


def create_user_with_exception():
    try:
        with transaction.atomic():
            user = User.objects.create(username="testuser")
            print("User created")
            # Simulate an error to force a rollback
            raise Exception("Simulating an error after user creation")
    except Exception as e:
        print(f"Error occurred: {e}")
