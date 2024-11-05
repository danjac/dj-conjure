import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import Client

from {{ project_slug }}.users.models import User
from {{ project_slug }}.users.tests.factories import UserFactory


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def anonymous_user() -> AnonymousUser:
    return AnonymousUser()


@pytest.fixture
def auth_user(client: Client, user: User) -> User:
    client.force_login(user)
    return user


@pytest.fixture
def staff_user(client: Client) -> User:
    user = UserFactory(is_staff=True)
    client.force_login(user)
    return user
