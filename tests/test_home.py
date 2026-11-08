import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_sys_p01_home_opens(client):
    """PG-01: главная страница открывается и содержит заголовок."""
    response = client.get(reverse("web:home"))
    assert response.status_code == 200
    assert "Карточка игрока" in response.content.decode()


@pytest.mark.django_db
def test_sys_g06_page_is_russian_html(client):
    """SYS-G06: страница на русском языке."""
    html = client.get(reverse("web:home")).content.decode()
    assert '<html lang="ru">' in html


@pytest.mark.django_db
def test_sys_g11_page_has_viewport(client):
    """SYS-G11: страница подходит для телефона (есть viewport)."""
    html = client.get(reverse("web:home")).content.decode()
    assert 'name="viewport"' in html
